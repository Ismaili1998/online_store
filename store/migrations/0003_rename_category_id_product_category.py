# Generated by Django 3.2.9 on 2022-04-04 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_updated_at_alter_product_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
    ]
