# Generated by Django 4.1.7 on 2023-06-23 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_cloud_1_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloud_1',
            name='Email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cloud'),
        ),
    ]
