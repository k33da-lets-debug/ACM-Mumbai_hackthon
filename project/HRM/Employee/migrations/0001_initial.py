# Generated by Django 3.0.3 on 2020-03-01 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(max_length=300)),
                ('emailId', models.EmailField(max_length=150)),
                ('phoneNo', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('designation', models.CharField(choices=[('EMP', 'Employee'), ('MGR', 'Manager')], default='EMP', max_length=50)),
                ('date_of_joining', models.DateField(auto_now_add=True)),
                ('date_of_birth', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
