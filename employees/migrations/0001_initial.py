# Generated by Django 3.0.3 on 2020-02-13 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, help_text='Contact phone number', max_length=200)),
                ('mail', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('salary', models.CharField(max_length=50)),
                ('position', models.CharField(blank=True, choices=[('a', 'accountant'), ('m', 'manager'), ('s', 'seller'), ('sa', 'sales assistant')], default='s', help_text='v', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('price', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('count', models.IntegerField()),
                ('type', models.CharField(blank=True, choices=[('c', 'computers'), ('l', 'laptops'), ('p', 'phones'), ('tv', 'TV')], default='', help_text='v', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
