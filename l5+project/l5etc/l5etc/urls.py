from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from users.auth_views import LoggedLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', LoggedLoginView.as_view(), name='login'),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
