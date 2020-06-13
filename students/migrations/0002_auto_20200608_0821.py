from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='dob1',
            new_name='dob',
        ),
        migrations.AddField(
            model_name='student',
            name='grade_while_joining',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
