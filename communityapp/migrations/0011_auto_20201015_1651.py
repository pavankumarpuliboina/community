# Generated by Django 3.1.2 on 2020-10-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityapp', '0010_auto_20201014_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
