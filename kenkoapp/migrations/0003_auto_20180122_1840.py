# Generated by Django 2.0.1 on 2018-01-22 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kenkoapp', '0002_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carepro',
            old_name='image',
            new_name='avatar',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='image',
        ),
    ]