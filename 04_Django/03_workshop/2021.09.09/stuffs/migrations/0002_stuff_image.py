# Generated by Django 3.2.7 on 2021-09-09 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuffs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuff',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]