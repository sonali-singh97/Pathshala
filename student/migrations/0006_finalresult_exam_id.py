# Generated by Django 3.0.5 on 2021-06-26 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_subjectresult_exam_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalresult',
            name='exam_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='student.Exam'),
            preserve_default=False,
        ),
    ]