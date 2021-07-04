from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AuthIndex


web_urls = [
    path('', AuthIndex.as_view(), name='auth'),
    path('sign-out/', auth_views.LogoutView.as_view(template_name='auth/login.html'), name='sign-out'),
]
