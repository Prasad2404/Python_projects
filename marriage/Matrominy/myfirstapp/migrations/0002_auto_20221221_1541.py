# Generated by Django 3.1.14 on 2022-12-21 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='about_profile',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='alternate_contact',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
