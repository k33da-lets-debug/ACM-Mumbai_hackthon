# Generated by Django 3.0.3 on 2020-03-07 17:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0008_meeting'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeWorkingHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today_date', models.DateField(default=datetime.datetime(2020, 3, 7, 17, 49, 5, 828845, tzinfo=utc))),
                ('start_time', models.TimeField(blank=True, default=None, null=True)),
                ('end_time', models.TimeField(blank=True, default=None, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
