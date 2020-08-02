# Generated by Django 3.0.3 on 2020-03-07 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0007_auto_20200307_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('date_of_meeting', models.DateField()),
                ('time_start', models.TimeField(blank=True, null=True)),
                ('time_end', models.TimeField(blank=True, null=True)),
                ('approval', models.CharField(choices=[('accept', 'accept'), ('pending', 'pending'), ('rejected', 'rejected')], default='pending', max_length=50)),
                ('included_in_salary', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
