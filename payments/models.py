from django.db import models


class Payment(models.Model):

    PAYMENT_METHODS = [
        ("pix", "Pix"),
        ("credit_card", "Credit Card"),
        ("debit_card", "Debit Card"),
    ]

    PAYMENT_STATUS = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("canceled", "Canceled"),
        ("refunded", "Refunded"),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    status = models.CharField(
        max_length=20, choices=PAYMENT_STATUS, default="pending"
    )
    reference_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Payment #{self.id} - {self.status}"


# Create your models here.
