# Generated by Django 2.2.3 on 2019-07-21 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_auto_20190721_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userdata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.Users'),
        ),
    ]
