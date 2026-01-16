from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now
from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @action(detail=True, methods=["patch"])
    def pay(self, request, pk=None):
        payment = self.get_object()

        if payment.status == "paid":
            return Response(
                {"detail": "Payment already paid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        payment.status = "paid"
        payment.paid_at = now()
        payment.save()

        serializer = self.get_serializer(payment)
        return Response(serializer.data)

# Create your views here.
