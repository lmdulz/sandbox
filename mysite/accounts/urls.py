from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('register/', views.register_view),
    #path('<int:pk>/', views.UserProfileView.as_view(), name='user_profile')
]