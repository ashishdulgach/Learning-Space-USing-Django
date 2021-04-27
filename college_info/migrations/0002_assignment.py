from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('submission_date', models.DateField()),
                ('doc', models.FileField(upload_to='assignments')),
                ('teach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_info.Teaches')),
            ],
        ),
    ]
