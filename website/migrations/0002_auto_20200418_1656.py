# Generated by Django 2.2.7 on 2020-04-18 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horatrabalhada',
            old_name='price',
            new_name='preco',
        ),
    ]
