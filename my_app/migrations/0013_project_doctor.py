# Generated by Django 4.0.6 on 2022-08-01 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0012_remove_project_doctor_project_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.doctor'),
        ),
    ]
