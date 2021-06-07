# Generated by Django 3.2.3 on 2021-05-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingyacht', '0005_alter_yachtreservation_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='yacht',
            name='category',
            field=models.IntegerField(choices=[(1, 'monohulls'), (2, 'catamarans'), (3, 'Motor Boat'), (4, 'Trimaran')], default=1),
            preserve_default=False,
        ),
    ]
