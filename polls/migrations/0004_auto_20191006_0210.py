# Generated by Django 2.2.6 on 2019-10-05 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20191005_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dl_model',
            name='Work_accident',
        ),
        migrations.RemoveField(
            model_name='dl_model',
            name='average_montly_hours',
        ),
        migrations.RemoveField(
            model_name='dl_model',
            name='department',
        ),
        migrations.RemoveField(
            model_name='dl_model',
            name='last_evaluation',
        ),
        migrations.RemoveField(
            model_name='dl_model',
            name='left',
        ),
        migrations.RemoveField(
            model_name='dl_model',
            name='number_project',
        ),
        migrations.RemoveField(
            model_name='dl_model',
            name='promotion_last_5years',
        ),
        migrations.RemoveField(
            model_name='dl_model',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='dl_model',
            name='satisfaction_level',
        ),
        migrations.RemoveField(
            model_name='dl_model',
            name='time_spend_company',
        ),
    ]
