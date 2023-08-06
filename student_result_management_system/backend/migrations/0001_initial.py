# Generated by Django 4.2.4 on 2023-08-06 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('family_name', models.CharField(max_length=120)),
                ('date_of_birth', models.DateField()),
                ('email_address', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.course')),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.score')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
    ]
