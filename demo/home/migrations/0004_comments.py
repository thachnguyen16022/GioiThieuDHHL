# Generated by Django 5.0 on 2024-01-02 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_giamhieu_anh'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('cmt_id', models.AutoField(primary_key=True, serialize=False)),
                ('cmt', models.CharField(max_length=1000)),
                ('ho_ten', models.CharField(max_length=50)),
            ],
        ),
    ]
