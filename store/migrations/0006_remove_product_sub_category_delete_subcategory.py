# Generated by Django 4.0 on 2023-06-25 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_subcategory_product_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sub_category',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]
