# Generated by Django 3.0.5 on 2021-07-06 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutAndStaffs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_video',
            field=models.FileField(default='school_vid.mp4', upload_to='video'),
            preserve_default=False,
        ),
    ]