# Generated by Django 4.2.6 on 2023-11-30 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_bookingreq_delete_userreq'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingreq',
            name='rstatus',
            field=models.TextField(default='pending'),
        ),
        migrations.AddField(
            model_name='bookingreq',
            name='tcost',
            field=models.IntegerField(default=500),
        ),
    ]
