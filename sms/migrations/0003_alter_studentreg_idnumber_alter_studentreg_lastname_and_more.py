# Generated by Django 4.0.3 on 2022-11-16 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_alter_studentreg_resultsslip_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreg',
            name='IDnumber',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='Lastname',
            field=models.CharField(max_length=26, null=True),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='StudentEmail',
            field=models.EmailField(max_length=42, null=True, unique=True),
        ),
    ]
