# Generated by Django 3.2.14 on 2022-12-21 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
