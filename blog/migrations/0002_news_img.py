# Generated by Django 3.0.3 on 2020-03-26 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='user_images'),
        ),
    ]
