# Generated by Django 3.1.2 on 2021-03-31 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=4)),
                ('genre', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=150)),
                ('year', models.CharField(max_length=4)),
                ('date', models.DateField(auto_now_add=True)),
                ('is_favorites', models.BooleanField(default=False)),
            ],
        ),
    ]
