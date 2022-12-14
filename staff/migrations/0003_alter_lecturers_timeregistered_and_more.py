# Generated by Django 4.0.3 on 2022-11-15 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_lecturers_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturers',
            name='Timeregistered',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='lecturers',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
