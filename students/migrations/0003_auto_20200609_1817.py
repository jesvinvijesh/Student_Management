from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20200608_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_image_url',
            field=models.ImageField(blank=True, null=True, upload_to='student_student_image_url/'),
        ),
    ]
