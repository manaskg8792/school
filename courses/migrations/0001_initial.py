# Generated by Django 3.2.9 on 2021-11-09 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('duration', models.IntegerField()),
                ('max_students', models.DecimalField(decimal_places=2, max_digits=14)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools_app.school')),
            ],
        ),
    ]
