from django.db import models


class Category(models.Model):
    name = models.CharField('категория', max_length=50)


class Product(models.Model):
    pass

