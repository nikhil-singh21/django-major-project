# Generated by Django 3.0.3 on 2020-02-06 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200206_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='authorname',
            new_name='username',
        ),
    ]
