# Generated by Django 3.0.3 on 2020-04-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='user',
            name='second_name',
            field=models.CharField(max_length=264),
        ),
    ]
