# Generated by Django 3.0.1 on 2020-01-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200121_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
    ]
