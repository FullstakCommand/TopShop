from django.db import models


class Category(models.Model):
    name = models.CharField('категория', max_length=50)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField(Category, verbose_name='категория')
    name = models.CharField('название товара', max_length=120)
    description = models.TextField('описание')
    item_number = models.BigIntegerField('номер товара', default=0)
    price = models.FloatField('цена', default=0.00)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.name


