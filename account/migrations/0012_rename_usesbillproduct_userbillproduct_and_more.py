# Generated by Django 4.0 on 2022-01-14 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('account', '0011_usesbillsubscription_usesbillproduct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UsesBillProduct',
            new_name='UserBillProduct',
        ),
        migrations.RenameModel(
            old_name='UsesBillSubscription',
            new_name='UserBillSubscription',
        ),
    ]