# Generated by Django 3.0.5 on 2021-12-25 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20210904_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_fees',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='student_fees',
            name='payment_date',
            field=models.DateTimeField(null=True),
        ),
    ]