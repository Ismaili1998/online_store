# Generated by Django 3.2.9 on 2022-04-08 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='method',
            field=models.CharField(default='paypal', max_length=50),
            preserve_default=False,
        ),
    ]
