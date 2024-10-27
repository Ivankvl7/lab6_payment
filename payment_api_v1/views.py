from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Profile
from django.shortcuts import get_object_or_404


class UserBalance(APIView):
    def get(self, request, format=None):
        user_slug = request.GET.get('user_slug')
        total_price = request.GET.get('total_price')
        if not user_slug:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        profile = get_object_or_404(Profile, slug=user_slug)
        balance = profile.available_cash
        if balance >= int(total_price):
            profile.available_cash = balance - int(total_price)
            profile.save()

            return Response({'balance': balance}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_402_PAYMENT_REQUIRED)

