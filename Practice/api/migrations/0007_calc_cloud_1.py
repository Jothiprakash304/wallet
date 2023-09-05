# Generated by Django 4.1.7 on 2023-06-22 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_parentmodel_person_table_childmodel_passport'),
    ]

    operations = [
        migrations.CreateModel(
            name='calc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_1', models.IntegerField()),
                ('num_2', models.IntegerField()),
            ],
            options={
                'db_table': 'Total',
            },
        ),
        migrations.CreateModel(
            name='Cloud_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField()),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cloud')),
            ],
            options={
                'db_table': 'amount_table',
            },
        ),
    ]