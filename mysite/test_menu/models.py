from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=512)

    def __str__(self):
        return self.category_name

class AboutUs(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}, {self.description}'


class ImageAboutUs(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE)
    image_about_us = models.ImageField(upload_to='about_us_images/', null=True, blank=True)


class Extras(models.Model):
    title = models.CharField(max_length=233)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.title}, {self.price}'

class FullMainMenu(models.Model):
    extras_name = models.ForeignKey(Extras, on_delete=models.CASCADE)
    title = models.CharField(max_length=233)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_menu = models.ImageField(upload_to='image_menu/', null=True, blank=True)

    def __str__(self):
        return f'{self.title} {self.price}'

