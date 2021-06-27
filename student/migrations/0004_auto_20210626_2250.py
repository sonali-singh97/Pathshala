# Generated by Django 3.0.5 on 2021-06-26 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_subjectresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='subjectresult',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='FinalResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obtained_marks', models.PositiveSmallIntegerField(default=0)),
                ('total_marks', models.PositiveSmallIntegerField(default=0)),
                ('percentage', models.PositiveSmallIntegerField(default=0)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.Student')),
            ],
        ),
    ]