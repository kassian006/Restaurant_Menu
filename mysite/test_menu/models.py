from django.db import models


class  BestSellers(models.Model):
    title = models.CharField(max_length=320)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}-{self.description}'


class BestSellerImage(models.Model):
    best_seller = models.ForeignKey(BestSellers, on_delete=models.CASCADE)
    best_seller_image = models.ImageField(upload_to='best_seller_image/', null=True, blank=True)

    def __str__(self):
        return f'{self.best_seller}-{self.best_seller_image}'


class MainMenu(models.Model):
    title = models.CharField(max_length=233)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.title}-{self.description}-{self.price}'


