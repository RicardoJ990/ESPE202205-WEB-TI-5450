# Generated by Django 4.0.6 on 2022-07-20 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=500)),
                ('Department', models.CharField(max_length=500)),
                ('DateOfJoining', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('ProductId', models.AutoField(primary_key=True, serialize=False)),
                ('ProductName', models.CharField(max_length=500)),
                ('ProductType', models.CharField(max_length=500)),
                ('DateOfExpiration', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('OrderId', models.AutoField(primary_key=True, serialize=False)),
                ('OrderName', models.CharField(max_length=500)),
                ('Product', models.CharField(max_length=500)),
                ('DateOfOrder', models.DateField()),
            ],
        ),
    ]
