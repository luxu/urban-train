# Generated by Django 2.2.7 on 2020-04-18 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200418_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horatrabalhada',
            old_name='preco',
            new_name='price',
        ),
    ]
