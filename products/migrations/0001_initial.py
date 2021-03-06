# Generated by Django 3.0.4 on 2020-04-09 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_categoty', models.CharField(max_length=500)),
                ('name_category', models.CharField(max_length=500)),
                ('image_category', models.ImageField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_product', models.CharField(max_length=500)),
                ('name_product', models.CharField(max_length=500)),
                ('describe', models.CharField(blank=True, max_length=500, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('main_picture', models.ImageField(default='', upload_to='')),
                ('price', models.IntegerField(default=0)),
                ('discount', models.FloatField(default=0)),
                ('num_available', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(related_name='CategoryOfProduct', to='products.Category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Who_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_product', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PictureOfProduct', to='products.Products')),
            ],
        ),
    ]
