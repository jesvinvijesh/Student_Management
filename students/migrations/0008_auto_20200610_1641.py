# Generated by Django 2.1.5 on 2020-06-10 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_student_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='contact_number1',
            new_name='phone',
        ),
    ]