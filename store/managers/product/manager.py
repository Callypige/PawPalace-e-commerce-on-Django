from django.db import models

class ProductManager(models.Manager):
    def available(self):
        return self.filter(is_available=True)

    def low_stock(self, threshold=5):
        return self.filter(stock__lt=threshold)