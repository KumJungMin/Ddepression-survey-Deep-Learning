# Generated by Django 3.0.2 on 2020-01-08 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snippet',
            new_name='Post',
        ),
    ]