# Generated by Django 3.1.2 on 2020-10-14 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityapp', '0008_auto_20201014_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(max_length=500),
        ),
    ]
