# Generated by Django 2.2.3 on 2019-07-21 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_auto_20190721_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='userdata',
        ),
    ]
