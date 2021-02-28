from django.db import models


class Category(models.Model):
    name = models.CharField('Категория', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Attr(models.Model):
    ean = models.IntegerField('штрихкод', blank=True)
    desc = models.TextField('дополнительное описание')

    class Meta:
        verbose_name = 'дополнительный атрибут'
        verbose_name_plural = 'дополнительные атрибуты'


# создаю базовый продукт
class Product(models.Model):
    category = models.ManyToManyField(Category, verbose_name='категория')
    name = models.CharField(verbose_name='Название товара', max_length=50)
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена', default=0.00)
    number = models.IntegerField(verbose_name='Номер товара', default=0)
    add_attributes = models.ManyToManyField(Attr, verbose_name='дополнительные атрибуты')
    amount = models.IntegerField('Количество')
    image = models.ImageField('Фото', width_field=150, height_field=150)

    def __str__(self):
        return f'{self.name}, {self.price}, {self.category}, {self.description},{self.number}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


# class ProductCategory(models.Model):
#   category = models.ForeignKey(Category, on_delete=models.CASCADE)
#    product = models.ForeignKey(Product, on_delete=models.CASCADE)
#    amount = models.IntegerField('Количество', default=0)

















