from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UsersLoginView.as_view(), name='user_login'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.userprofile_view, name='user_profile'),

    path('logout/', views.LogoutUser.as_view(), name='logout_user'),
]