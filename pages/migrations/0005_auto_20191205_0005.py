# Generated by Django 2.2.7 on 2019-12-04 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20191205_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagecard',
            old_name='slideImage',
            new_name='cardImage',
        ),
    ]
