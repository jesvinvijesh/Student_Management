from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20200612_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='inst_student_id',
            new_name='student_id',
        ),
    ]
