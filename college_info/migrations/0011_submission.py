

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_info', '0010_marks_marksclass_studentcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(upload_to='submissions')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_info.Assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_info.Student')),
            ],
        ),
    ]
