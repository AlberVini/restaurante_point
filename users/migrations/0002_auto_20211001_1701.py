# Generated by Django 3.2.7 on 2021-10-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='adress',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='dt_birth',
            field=models.DateField(null=True),
        ),
    ]
