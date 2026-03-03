from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
]