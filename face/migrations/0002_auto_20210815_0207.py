# Generated by Django 3.2.5 on 2021-08-15 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='word',
            new_name='password',
        ),
        migrations.AlterField(
            model_name='app',
            name='number',
            field=models.IntegerField(),
        ),
    ]
