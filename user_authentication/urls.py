from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('user/<int:pk>/', views.get_user, name='get_user'),
    path('user/', views.get_all_user, name='get_all_user'),
    path('user/update/<int:pk>/', views.update_user, name='update_user'),
    path('user/delete/<int:pk>/', views.delete_user, name='delete_user'),
    # JWT Token Login/Obtain endpoint
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
