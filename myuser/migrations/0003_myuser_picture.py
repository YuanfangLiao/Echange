# Generated by Django 2.1.7 on 2019-04-20 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_auto_20190405_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='picture',
            field=models.CharField(default='img/timg.jpg', max_length=500, verbose_name='头像'),
        ),
    ]
