# Generated by Django 3.2.7 on 2021-10-01 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211001_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dt_birth',
            new_name='data_nascimento',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='adress',
            new_name='endereco',
        ),
    ]