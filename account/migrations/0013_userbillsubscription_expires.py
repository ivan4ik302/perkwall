# Generated by Django 4.0 on 2022-01-14 11:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_rename_usesbillproduct_userbillproduct_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbillsubscription',
            name='expires',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
