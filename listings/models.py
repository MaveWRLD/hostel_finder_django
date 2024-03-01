import secrets
from django.db import models
from .paystack import Paystack


class Listing(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    hostel_name = models.CharField(max_length=100)
    hostel_price = models.DecimalField(max_digits=10, decimal_places=2)
    ref = models.CharField(max_length=200, )
    #booking_number = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'listing {self.id}'

    def hostel_price_value(self) -> int:
        return self.hostel_price * 100

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Listing.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.hostel_price)
        if status:
            if result['amount'] / 100 == self.hostel_price:
                self.paid = True
            self.save()
        if self.paid:
            return True
        return False

# Create your models here.
