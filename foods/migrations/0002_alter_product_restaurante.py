# Generated by Django 3.2.7 on 2021-10-14 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211014_1628'),
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='restaurante',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.restaurant'),
        ),
    ]
