# Generated by Django 2.1.1 on 2018-09-04 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mylost', '0007_auto_20180905_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
