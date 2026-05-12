import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from pytest_django.asserts import assertRedirects

from users.models import FriendRequest

pytestmark = pytest.mark.django_db


def register_data(**kwargs):
    data = {
        'username': 'new_user',
        'email': 'new_user@example.com',
        'phone': '+79999999999',
        'password1': 'StrongTestPassword123',
        'password2': 'StrongTestPassword123',
    }
    data.update(kwargs)
    return data


def test_register_creates_user_and_logs_in(client, django_user_model):
    response = client.post(reverse('register'), register_data())

    assertRedirects(response, reverse('home'))
    user = django_user_model.objects.get(username='new_user')
    assert user.email == 'new_user@example.com'
    assert user.phone == '+79999999999'
    assert str(client.session['_auth_user_id']) == str(user.pk)


@pytest.mark.parametrize(
    'field,value',
    [
        ('username', 'test_user'),
        ('email', 'test_user@example.com'),
        ('phone', '+70000000001'),
    ],
)
def test_register_duplicate_fields_show_errors(client, user, field, value, django_user_model):
    response = client.post(reverse('register'), register_data(**{field: value}))

    assert response.status_code == 200
    assert field in response.context['form'].errors
    assert django_user_model.objects.filter(username='new_user').count() == 0


def test_login_success(client, user, password):
    response = client.post(reverse('login'), {'username': user.username, 'password': password})

    assertRedirects(response, reverse('home'))
    assert str(client.session['_auth_user_id']) == str(user.pk)


def test_logout_success(auth_client):
    response = auth_client.post(reverse('logout'))

    assertRedirects(response, reverse('home'))
    assert '_auth_user_id' not in auth_client.session


def test_authenticated_user_redirected_from_register(auth_client):
    response = auth_client.get(reverse('register'))

    assertRedirects(response, reverse('profile'))


@pytest.mark.parametrize('url_name', ['profile', 'profile_edit', 'user_list'])
def test_anonymous_user_redirected_from_private_pages(client, url_name):
    url = reverse(url_name)
    response = client.get(url)

    assertRedirects(response, f'{reverse("login")}?next={url}')


def test_user_can_open_own_profile(auth_client):
    response = auth_client.get(reverse('profile'))

    assert response.status_code == 200


def test_user_cannot_open_stranger_profile(auth_client, other_user):
    response = auth_client.get(reverse('user_profile', args=[other_user.pk]))

    assert response.status_code == 403


def test_user_can_send_friend_request(auth_client, user, other_user):
    response = auth_client.post(reverse('send_friend_request', args=[other_user.pk]))

    assertRedirects(response, reverse('user_list'))
    assert FriendRequest.objects.filter(from_user=user, to_user=other_user).exists()
    assert not user.friends.filter(pk=other_user.pk).exists()


def test_duplicate_friend_request_is_not_created(auth_client, user, other_user):
    auth_client.post(reverse('send_friend_request', args=[other_user.pk]))
    auth_client.post(reverse('send_friend_request', args=[other_user.pk]))

    assert FriendRequest.objects.filter(from_user=user, to_user=other_user).count() == 1


def test_friend_request_receiver_can_accept(client, user, other_user):
    friend_request = FriendRequest.objects.create(from_user=user, to_user=other_user)
    client.force_login(other_user)

    response = client.post(reverse('accept_friend_request', args=[friend_request.pk]))

    assertRedirects(response, reverse('user_list'))
    assert other_user.friends.filter(pk=user.pk).exists()
    assert user.friends.filter(pk=other_user.pk).exists()
    assert not FriendRequest.objects.filter(pk=friend_request.pk).exists()


def test_friend_request_receiver_can_decline(client, user, other_user):
    friend_request = FriendRequest.objects.create(from_user=user, to_user=other_user)
    client.force_login(other_user)

    response = client.post(reverse('decline_friend_request', args=[friend_request.pk]))

    assertRedirects(response, reverse('user_list'))
    assert not other_user.friends.filter(pk=user.pk).exists()
    assert not FriendRequest.objects.filter(pk=friend_request.pk).exists()


def test_user_cannot_accept_request_for_another_user(auth_client, other_user, third_user):
    friend_request = FriendRequest.objects.create(from_user=other_user, to_user=third_user)

    response = auth_client.post(reverse('accept_friend_request', args=[friend_request.pk]))

    assert response.status_code == 404
    assert not other_user.friends.filter(pk=third_user.pk).exists()


def test_friend_profile_available_after_accept(auth_client, user, other_user):
    user.friends.add(other_user)

    response = auth_client.get(reverse('user_profile', args=[other_user.pk]))

    assert response.status_code == 200


def test_user_can_remove_friend(auth_client, user, other_user):
    user.friends.add(other_user)

    response = auth_client.post(reverse('remove_friend', args=[other_user.pk]))

    assertRedirects(response, reverse('profile'))
    assert not user.friends.filter(pk=other_user.pk).exists()
    assert not other_user.friends.filter(pk=user.pk).exists()


def test_profile_rejects_not_image_avatar(auth_client):
    not_image = SimpleUploadedFile('avatar.txt', b'not an image', content_type='text/plain')

    response = auth_client.post(
        reverse('profile_edit'),
        {
            'first_name': '',
            'last_name': '',
            'email': 'test_user@example.com',
            'phone': '+70000000001',
            'avatar': not_image,
        },
    )

    assert response.status_code == 200
    assert 'avatar' in response.context['form'].errors
