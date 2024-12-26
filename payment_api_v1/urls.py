from .views import PaymentListCreateView
from django.urls import path


urlpatterns = [
    path('payment/', PaymentListCreateView.as_view())
]