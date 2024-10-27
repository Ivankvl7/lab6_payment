from .views import UserBalance
from django.urls import path


urlpatterns = [
    path('user_balance/', UserBalance.as_view())
]