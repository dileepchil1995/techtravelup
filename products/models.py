from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/images/')
    category = models.CharField(max_length=255)
    url = models.URLField()
    rating = models.FloatField(default=0.0)
    verified = models.BooleanField(default=False)
    companyName = models.CharField(max_length=255)
    offer_start_date = models.DateField()
    offer_end_date = models.DateField()
    postedby = models.CharField(max_length=255)
    reelImage = models.ImageField(upload_to='products/reels/')
    reelStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.title