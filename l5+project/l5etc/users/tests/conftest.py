import pytest


@pytest.fixture
def password():
    return 'StrongTestPassword123'


@pytest.fixture
def user(django_user_model, password):
    return django_user_model.objects.create_user(
        username='test_user',
        email='test_user@example.com',
        phone='+70000000001',
        password=password,
    )


@pytest.fixture
def other_user(django_user_model, password):
    return django_user_model.objects.create_user(
        username='other_user',
        email='other_user@example.com',
        phone='+70000000002',
        password=password,
    )


@pytest.fixture
def third_user(django_user_model, password):
    return django_user_model.objects.create_user(
        username='third_user',
        email='third_user@example.com',
        phone='+70000000003',
        password=password,
    )


@pytest.fixture
def auth_client(client, user):
    client.force_login(user)
    return client
