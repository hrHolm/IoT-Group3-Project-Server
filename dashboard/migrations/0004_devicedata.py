# Generated by Django 3.0.5 on 2020-05-08 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20200506_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.FloatField()),
                ('light_value', models.FloatField()),
                ('setpoint_value', models.FloatField()),
                ('intensity_value', models.FloatField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Device')),
            ],
        ),
    ]