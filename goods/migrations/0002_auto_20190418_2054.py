# Generated by Django 2.1.7 on 2019-04-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='detail',
            field=models.TextField(max_length=2000, verbose_name='详细介绍'),
        ),
    ]
