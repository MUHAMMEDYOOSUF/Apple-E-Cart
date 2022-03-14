from django.db import models

# Create your models here.
from cartapp.models import product


class cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'cart'
        ordering = ['date_added']

    def __str__(self):
        return '{}'.format(self.cart_id)


class cartitem(models.Model):
    products = models.ForeignKey(product, on_delete=models.CASCADE)
    c = models.ForeignKey(cart, on_delete=models.CASCADE)
    qty = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'cartitem'

    def sub_total(self):
        return self.products.price * self.qty
    def __str__(self):
        return '{}'.format(self.products)
