# Generated by Django 4.2.4 on 2023-08-31 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('salt', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
