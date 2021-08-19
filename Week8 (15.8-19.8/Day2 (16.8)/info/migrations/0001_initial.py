# Generated by Django 3.2.6 on 2021-08-16 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='dane_joe', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('legs', models.IntegerField(default=4)),
                ('weight', models.IntegerField(default=100)),
                ('height', models.IntegerField(default=100)),
                ('speed', models.IntegerField(default=10)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='info.family')),
            ],
        ),
    ]
