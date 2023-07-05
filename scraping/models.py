from django.db import models


class YarnProduct(models.Model):
    GTIN = models.PositiveBigIntegerField(unique=True, null=True)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, null=True)
    needle_size = models.CharField(max_length=200, null=True)
    composition = models.CharField(max_length=200, null=True)
    lowest_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    historical_lowest_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WebResource(models.Model):
    yarn_product = models.ForeignKey(YarnProduct, on_delete=models.CASCADE, related_name='resources')
    url = models.URLField(max_length=200)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    available = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        availability = 'Available now' if self.available else 'Not available'
        return '%s: %s€ | %s | Last updated: %s' % (
            self.url, self.current_price, availability, self.updated_at.strftime("%d/%m/%Y, %H:%M:%S"))
