# Generated by Django 3.0.3 on 2020-03-07 21:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0011_auto_20200308_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='today_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 7, 21, 16, 30, 642848, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('leaves_taken', models.IntegerField(default=0)),
                ('deducted_salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('reimbursement', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total_salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]