# Generated by Django 2.2.13 on 2021-01-18 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_remove_thesis_course_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesis',
            name='author_id',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Students'),
            preserve_default=False,
        ),
    ]