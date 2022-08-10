# Generated by Django 4.0.6 on 2022-07-21 12:45

from django.db import migrations, models
import plan.models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_alter_event_depends_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('is waiting', 'IS_WAITING'), ('in progress', 'IN_PROGRESS'), ('finished', 'FINISHED'), ('expired', 'EXPIRED'), ('blocked', 'BLOCKED')], default=plan.models.Status['IN_PROGRESS'], max_length=20),
        ),
    ]
