# Generated by Django 4.2.5 on 2023-10-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='status',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
