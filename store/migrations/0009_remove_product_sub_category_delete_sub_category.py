# Generated by Django 4.0 on 2023-06-25 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_subcategory_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sub_category',
        ),
        migrations.DeleteModel(
            name='Sub_category',
        ),
    ]