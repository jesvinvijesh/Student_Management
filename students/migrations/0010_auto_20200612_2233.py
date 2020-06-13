from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20200612_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contact_number2',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.TextField(choices=[('Male', 'Male'), ('Female', 'Female')], default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='student',
            name='upload_student_image',
            field=models.ImageField(default=11, upload_to='student_student_image_url/'),
            preserve_default=False,
        ),
    ]
