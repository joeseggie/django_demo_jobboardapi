# Generated by Django 2.2.3 on 2019-07-13 09:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=120)),
                ('company_email', models.EmailField(max_length=60)),
                ('job_title', models.CharField(max_length=120)),
                ('job_description', models.CharField(max_length=120)),
                ('salary', models.FloatField()),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'job',
            },
        ),
    ]
