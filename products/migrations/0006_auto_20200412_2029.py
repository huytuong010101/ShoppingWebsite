# Generated by Django 3.0.4 on 2020-04-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200412_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug_product',
            field=models.SlugField(default='', max_length=500, unique=True),
        ),
    ]