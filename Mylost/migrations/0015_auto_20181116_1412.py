# Generated by Django 2.1.1 on 2018-11-16 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mylost', '0014_reportmodel_device_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportmodel',
            name='device_status',
            field=models.CharField(choices=[('FOUND', 'FOUND'), ('NOT FOUND', 'NOT FOUND')], default='NOT FOUND', max_length=20),
        ),
    ]
