# Generated by Django 4.0.3 on 2022-11-15 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
        ('payment', '0003_alter_payment_telephone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
        migrations.AlterUniqueTogether(
            name='feesdata',
            unique_together={('student_id', 'semester_id')},
        ),
    ]