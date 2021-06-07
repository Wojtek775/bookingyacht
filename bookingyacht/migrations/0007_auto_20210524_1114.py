# Generated by Django 3.2.3 on 2021-05-24 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingyacht', '0006_yacht_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yacht',
            name='yacht_category',
        ),
        migrations.AlterField(
            model_name='yachtreservation',
            name='yacht',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingyacht.yacht'),
        ),
        migrations.DeleteModel(
            name='YachtCategory',
        ),
    ]