from django.urls import path
from django.http import HttpResponse
from accounts.views import SignUpView, ProfileUpdateView, ProfileDetailView, LoginView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('user/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
]