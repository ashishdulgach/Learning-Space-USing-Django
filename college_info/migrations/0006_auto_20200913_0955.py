
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_info', '0005_auto_20200912_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date(2020, 9, 13)),
        ),
        migrations.CreateModel(
            name='AttendanceTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_info.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_info.Student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
    ]
