# Generated by Django 2.1.7 on 2019-04-05 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='sex',
            field=models.IntegerField(choices=[(1, '男'), (2, '女')], default=1),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'normal'), (2, 'admin')], default=1),
        ),
    ]