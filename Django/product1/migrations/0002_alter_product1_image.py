# Generated by Django 4.2.5 on 2023-10-20 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product1',
            name='image',
            field=models.ImageField(upload_to='product1s/'),
        ),
    ]
