# Generated by Django 2.1.5 on 2020-06-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20200609_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_image_url',
            field=models.ImageField(blank=True, null=True, upload_to='directory'),
        ),
    ]
