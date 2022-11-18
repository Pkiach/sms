# Generated by Django 4.0.3 on 2022-11-13 07:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semesterfees',
            fields=[
                ('semester', models.IntegerField(primary_key=True, serialize=False)),
                ('fees', models.IntegerField()),
                ('year', models.CharField(max_length=14)),
                ('status', models.CharField(default='false', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('telephone_number', models.CharField(max_length=16)),
                ('amount_paid', models.IntegerField()),
                ('status', models.CharField(default='INCOMPLETE', max_length=16)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('student_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.studentreg')),
            ],
        ),
    ]