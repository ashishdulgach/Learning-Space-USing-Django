

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('college_info', '0007_auto_20200913_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 13, 4, 29, 15, 821489, tzinfo=utc)),
        ),
    ]
