from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20200610_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_image_url',
            new_name='upload_student_image',
        ),
    ]
