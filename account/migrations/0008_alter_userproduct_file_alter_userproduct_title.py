# Generated by Django 4.0 on 2021-12-31 10:26

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20211228_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproduct',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=account.models.custom_file_name),
        ),
        migrations.AlterField(
            model_name='userproduct',
            name='title',
            field=models.TextField(max_length=210),
        ),
    ]