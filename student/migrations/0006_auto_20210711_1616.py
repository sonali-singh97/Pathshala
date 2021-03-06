# Generated by Django 3.0.5 on 2021-07-11 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_finalresult_class_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='contact_number',
            new_name='father_contact',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_id',
            new_name='roll_number',
        ),
        migrations.AddField(
            model_name='student',
            name='mother_contact',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='total_present',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='total_working_days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='transport_facility',
            field=models.BooleanField(default=False),
        ),
    ]
