# Generated by Django 3.2.7 on 2021-09-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210927_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='first_quarter',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='second_quarter',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='third_quarter',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='yearly',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='text_content',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
