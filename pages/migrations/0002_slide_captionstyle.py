# Generated by Django 2.2.7 on 2019-11-25 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='captionStyle',
            field=models.CharField(choices=[('caption left-align', 'Baslık Solda'), ('caption right-align', 'Baslık Sagda'), ('caption center-align', 'Baslık Ortada')], max_length=15, null=True),
        ),
    ]
