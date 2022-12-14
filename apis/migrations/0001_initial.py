# Generated by Django 4.1.2 on 2022-10-06 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('assignedDate', models.DateField()),
                ('resource', models.CharField(blank=True, default='', max_length=100)),
                ('priority', models.CharField(choices=[('average', 'Average'), ('high', 'High'), ('low', 'Low')], default='Low', max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
