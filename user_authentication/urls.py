from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('user/<int:pk>/', views.get_user, name='get_user'),
    path('user/', views.get_all_user, name='get_all_user'),
    path('user/update/<int:pk>/', views.update_user, name='update_user'),
    path('user/delete/<int:pk>/', views.delete_user, name='delete_user'),
]