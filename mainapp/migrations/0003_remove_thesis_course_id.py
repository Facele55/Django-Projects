# Generated by Django 2.2.13 on 2021-01-18 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210109_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thesis',
            name='course_id',
        ),
    ]
