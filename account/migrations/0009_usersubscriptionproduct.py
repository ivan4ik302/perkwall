# Generated by Django 4.0 on 2022-01-12 06:20

import account.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('account', '0008_alter_userproduct_file_alter_userproduct_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubscriptionProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=21)),
                ('title', models.TextField(max_length=210)),
                ('body', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to=account.models.custom_file_name)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.usersubscription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
