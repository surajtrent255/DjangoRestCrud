# Generated by Django 3.2.4 on 2021-06-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]