# Generated by Django 5.0.7 on 2024-07-20 18:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewsmodel',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
