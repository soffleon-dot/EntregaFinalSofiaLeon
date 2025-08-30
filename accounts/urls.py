from django.urls import path
from .views import signup, SignInView, PasswordChangeSimpleView, profile, logout_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', profile, name='profile'),
    path('password-change/', PasswordChangeSimpleView.as_view(), name='password_change'),
]
