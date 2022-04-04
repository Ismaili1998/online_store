# Generated by Django 4.0.3 on 2022-04-01 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('price', models.IntegerField()),
                ('is_available', models.BooleanField()),
                ('image', models.ImageField(upload_to='photos/products')),
                ('stock', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
