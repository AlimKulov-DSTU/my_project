import logging

from django.contrib.auth.views import LoginView

logger = logging.getLogger(__name__)


class LoggedLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        logger.info('User %s logged in', username)
        return super().form_valid(form)

    def form_invalid(self, form):
        username = self.request.POST.get('username', '')
        logger.warning('Failed login attempt for %s', username)
        return super().form_invalid(form)
