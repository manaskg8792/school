# Generated by Django 3.2.9 on 2021-11-10 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20211110_0612'),
        ('schools_app', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Students',
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.courses'),
        ),
    ]