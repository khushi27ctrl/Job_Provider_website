# Generated by Django 3.2.7 on 2021-12-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20211212_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, default='00000', max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, default='00000', max_length=122),
        ),
    ]