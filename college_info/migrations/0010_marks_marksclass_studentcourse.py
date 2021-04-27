
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_info', '0009_auto_20200913_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_info.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_info.Student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.CreateModel(
            name='MarksClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Insem', 'Insem'), ('Term Work', 'Term Work')], max_length=50)),
                ('status', models.BooleanField(default='False')),
                ('teach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_info.Teaches')),
            ],
            options={
                'unique_together': {('teach', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Insem', 'Insem'), ('Term Work', 'Term Work')], max_length=50)),
                ('marks', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('student_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_info.StudentCourse')),
            ],
            options={
                'unique_together': {('student_course', 'name')},
            },
        ),
    ]
