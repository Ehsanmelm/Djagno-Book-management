# Generated by Django 5.0.7 on 2024-07-21 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_booksmodel_table_alter_reviewsmodel_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='booksmodel',
            table='books',
        ),
        migrations.AlterModelTable(
            name='reviewsmodel',
            table='review',
        ),
    ]
