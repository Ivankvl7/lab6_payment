from .views import PaymentListCreateView
from django.urls import path


urlpatterns = [
    path('payment_proceed/', PaymentListCreateView.as_view())
]