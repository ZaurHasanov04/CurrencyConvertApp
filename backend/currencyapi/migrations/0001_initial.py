# Generated by Django 5.0.6 on 2024-05-26 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=80)),
                ('nominal', models.IntegerField()),
                ('value', models.DecimalField(decimal_places=4, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='UpdateApiDateTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'DateTime of Updating API',
            },
        ),
    ]