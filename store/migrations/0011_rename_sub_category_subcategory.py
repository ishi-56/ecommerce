# Generated by Django 4.0 on 2023-07-16 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_sub_category_product_sub_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sub_category',
            new_name='SubCategory',
        ),
    ]