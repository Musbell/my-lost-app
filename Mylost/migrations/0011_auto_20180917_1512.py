# Generated by Django 2.1.1 on 2018-09-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mylost', '0010_auto_20180916_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('ABUJA', 'ABUJA '), ('ABIA', 'ABIA'), ('ADAMAWA', 'ADAMAWA'), ('AKWA IBOM', 'AKWA IBOM'), ('ANAMBRA', 'ANAMBRA'), ('BAUCHI', 'BAUCHI'), ('BAYELSA', 'BAYELSA'), ('BENUE', 'BENUE'), ('BORNO', 'BORNO'), ('CROSS RIVER', 'CROSS RIVER'), ('DELTA', 'DELTA'), ('EBONYI', 'EBONYI'), ('ENUGU', 'ENUGU'), ('EDO', 'EDO'), ('EKITI', 'EKITI'), ('GOMBE', 'GOMBE'), ('IMO', 'IMO'), ('JIGAWA', 'JIGAWA'), ('KADUNA', 'KADUNA'), ('KANO', 'KANO'), ('KATSINA', 'KATSINA'), ('KEBBI', 'KEBBI'), ('KOGI', 'KOGI'), ('KWARA', 'KWARA'), ('LAGOS', 'LAGOS'), ('NASARAWA', 'NASARAWA'), ('NIGER', 'NIGER'), ('OGUN', 'OGUN'), ('ONDO', 'ONDO'), ('OSUN', 'OSUN'), ('OYO', 'OYO'), ('PLATEAU', 'PLATEAU'), ('RIVERS', 'RIVERS'), ('SOKOTO', 'SOKOTO'), ('YOBE', 'YOBE'), ('ZAMFARA', 'ZAMFARA')], default='', max_length=250)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(default=0, max_length=15)),
                ('short_bio', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='reportmodel',
            name='state',
            field=models.CharField(choices=[('ABUJA', 'ABUJA '), ('ABIA', 'ABIA'), ('ADAMAWA', 'ADAMAWA'), ('AKWA IBOM', 'AKWA IBOM'), ('ANAMBRA', 'ANAMBRA'), ('BAUCHI', 'BAUCHI'), ('BAYELSA', 'BAYELSA'), ('BENUE', 'BENUE'), ('BORNO', 'BORNO'), ('CROSS RIVER', 'CROSS RIVER'), ('DELTA', 'DELTA'), ('EBONYI', 'EBONYI'), ('ENUGU', 'ENUGU'), ('EDO', 'EDO'), ('EKITI', 'EKITI'), ('GOMBE', 'GOMBE'), ('IMO', 'IMO'), ('JIGAWA', 'JIGAWA'), ('KADUNA', 'KADUNA'), ('KANO', 'KANO'), ('KATSINA', 'KATSINA'), ('KEBBI', 'KEBBI'), ('KOGI', 'KOGI'), ('KWARA', 'KWARA'), ('LAGOS', 'LAGOS'), ('NASARAWA', 'NASARAWA'), ('NIGER', 'NIGER'), ('OGUN', 'OGUN'), ('ONDO', 'ONDO'), ('OSUN', 'OSUN'), ('OYO', 'OYO'), ('PLATEAU', 'PLATEAU'), ('RIVERS', 'RIVERS'), ('SOKOTO', 'SOKOTO'), ('YOBE', 'YOBE'), ('ZAMFARA', 'ZAMFARA')], default='', max_length=250),
        ),
    ]
