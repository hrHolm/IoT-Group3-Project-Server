# Generated by Django 3.0.5 on 2020-05-01 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SetpointData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.FloatField()),
                ('value', models.FloatField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Device')),
            ],
        ),
        migrations.CreateModel(
            name='LightData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.FloatField()),
                ('value', models.FloatField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Device')),
            ],
        ),
    ]
