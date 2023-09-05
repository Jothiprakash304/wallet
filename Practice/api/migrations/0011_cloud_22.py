# Generated by Django 4.1.7 on 2023-06-23 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_cloud_1_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloud_22',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField()),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cloud_2')),
            ],
            options={
                'db_table': 'amount_table_1',
            },
        ),
    ]
