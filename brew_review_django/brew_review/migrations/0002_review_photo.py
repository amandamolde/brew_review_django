# Generated by Django 2.1 on 2018-08-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew_review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='photo',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]