import logging

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView

from .forms import ProfileForm, RegisterForm
from .models import FriendRequest, User

logger = logging.getLogger(__name__)


class HomeView(TemplateView):
    template_name = 'home.html'


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        logger.info('User %s registered', self.object.username)
        return response

    def form_invalid(self, form):
        logger.warning('Registration validation error: %s', form.errors.as_json())
        return super().form_invalid(form)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.exclude(pk=self.request.user.pk).order_by('username')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outgoing_request_ids'] = list(
            self.request.user.sent_friend_requests.values_list('to_user_id', flat=True)
        )
        context['incoming_request_ids'] = list(
            self.request.user.received_friend_requests.values_list('from_user_id', flat=True)
        )
        context['incoming_requests'] = self.request.user.received_friend_requests.select_related('from_user')
        return context


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'profile_user'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        user = self.request.user if pk is None else get_object_or_404(User, pk=pk)
        if user != self.request.user and not self.request.user.friends.filter(pk=user.pk).exists():
            logger.warning('User %s tried to open private profile %s', self.request.user.username, user.username)
            raise PermissionDenied
        return user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object == self.request.user:
            context['incoming_requests'] = self.request.user.received_friend_requests.select_related('from_user')
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        logger.info('User %s updated profile', self.request.user.username)
        return super().form_valid(form)


class SendFriendRequestView(LoginRequiredMixin, View):
    def post(self, request, pk):
        to_user = get_object_or_404(User, pk=pk)
        reverse_request_exists = FriendRequest.objects.filter(from_user=to_user, to_user=request.user).exists()
        if (
            to_user != request.user
            and not request.user.friends.filter(pk=to_user.pk).exists()
            and not reverse_request_exists
        ):
            FriendRequest.objects.get_or_create(from_user=request.user, to_user=to_user)
            logger.info('User %s sent friend request to %s', request.user.username, to_user.username)
        else:
            logger.warning('User %s failed to send friend request to %s', request.user.username, to_user.username)
        return redirect('user_list')


class AcceptFriendRequestView(LoginRequiredMixin, View):
    def post(self, request, pk):
        friend_request = get_object_or_404(FriendRequest, pk=pk, to_user=request.user)
        from_user = friend_request.from_user
        request.user.friends.add(from_user)
        friend_request.delete()
        logger.info('User %s accepted friend request from %s', request.user.username, from_user.username)
        return redirect('user_list')


class DeclineFriendRequestView(LoginRequiredMixin, View):
    def post(self, request, pk):
        friend_request = get_object_or_404(FriendRequest, pk=pk, to_user=request.user)
        from_user = friend_request.from_user
        friend_request.delete()
        logger.info('User %s declined friend request from %s', request.user.username, from_user.username)
        return redirect('user_list')


class RemoveFriendView(LoginRequiredMixin, View):
    def post(self, request, pk):
        friend = get_object_or_404(User, pk=pk)
        if request.user.friends.filter(pk=friend.pk).exists():
            request.user.friends.remove(friend)
            logger.info('User %s removed friend %s', request.user.username, friend.username)
        else:
            logger.warning('User %s tried to remove non-friend %s', request.user.username, friend.username)
        return redirect('profile')
