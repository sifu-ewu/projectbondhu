# Generated by Django 4.0.6 on 2022-07-30 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_demo_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='max_def',
            field=models.IntegerField(default=1),
        ),
    ]
