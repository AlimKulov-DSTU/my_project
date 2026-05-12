from django.urls import path

from .views import (
    AcceptFriendRequestView,
    DeclineFriendRequestView,
    HomeView,
    ProfileUpdateView,
    ProfileView,
    RegisterView,
    RemoveFriendView,
    SendFriendRequestView,
    UserListView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', ProfileView.as_view(), name='user_profile'),
    path('users/<int:pk>/send-friend-request/', SendFriendRequestView.as_view(), name='send_friend_request'),
    path('users/<int:pk>/remove-friend/', RemoveFriendView.as_view(), name='remove_friend'),
    path('friend-requests/<int:pk>/accept/', AcceptFriendRequestView.as_view(), name='accept_friend_request'),
    path('friend-requests/<int:pk>/decline/', DeclineFriendRequestView.as_view(), name='decline_friend_request'),
]
