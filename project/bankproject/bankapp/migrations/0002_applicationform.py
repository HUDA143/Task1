# Generated by Django 4.1.5 on 2023-01-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(max_length=8)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('phone', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('account', models.CharField(max_length=100)),
                ('materials', models.CharField(max_length=100)),
            ],
        ),
    ]