from payment_api_v1 import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Profile
from django.shortcuts import get_object_or_404
from rest_framework import generics

from payment.models import Payment


class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

    def post(self, request, *args, **kwargs):
        user_slug = request.data.get('user_slug')
        total_price = request.data.get('total_price')

        if not user_slug:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        profile = get_object_or_404(Profile, slug=user_slug)
        balance = profile.available_cash
        if balance >= int(total_price):
            profile.available_cash = balance - int(total_price)
            profile.save()

            # Создаем запись в таблице Payment
            payment = Payment.objects.create(
                customer=profile.user,
                amount=total_price,
                status='S'  # Успешный статус
            )

            return Response({'balance': profile.available_cash, 'payment_id': payment.id}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_402_PAYMENT_REQUIRED)



