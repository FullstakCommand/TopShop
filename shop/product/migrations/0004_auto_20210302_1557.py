# Generated by Django 3.1.7 on 2021-03-02 15:57

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210302_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, height_field=150, upload_to='media', width_field=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='set_attrs',
            field=models.JSONField(default=product.models.my_attrs),
        ),
    ]
