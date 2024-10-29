from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['created_at', 'customer', 'amount', 'status']
