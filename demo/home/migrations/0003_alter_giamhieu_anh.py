# Generated by Django 5.0 on 2023-12-29 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_giamhieu_anh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giamhieu',
            name='anh',
            field=models.ImageField(default=None, upload_to='img'),
        ),
    ]