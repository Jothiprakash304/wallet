# Generated by Django 4.1.7 on 2023-06-19 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_pro_employee_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='hello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('n_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='hello_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='hari', max_length=100)),
                ('a_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hello')),
            ],
        ),
        migrations.DeleteModel(
            name='pro',
        ),
        migrations.DeleteModel(
            name='Employee_1',
        ),
    ]
