# Generated by Django 5.0 on 2023-12-29 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='giamhieu',
            name='anh',
            field=models.ImageField(default=None, upload_to='image'),
        ),
    ]
