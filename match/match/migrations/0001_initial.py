# Generated by Django 3.1.5 on 2021-01-26 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('alt_first_name', models.CharField(blank=True, max_length=100)),
                ('alt_last_name', models.CharField(blank=True, max_length=100)),
                ('province', models.CharField(choices=[('NL', 'Newfoundland and Labrador'), ('PE', 'Prince Edward Island'), ('NS', 'Nova Scotia'), ('NB', 'New Brunswick'), ('QC', 'Quebec'), ('ON', 'Ontario'), ('MB', 'Manitoba'), ('SK', 'Saskatchewan'), ('AB', 'Alberta'), ('BC', 'British Columbia'), ('YT', 'Yukon'), ('NT', 'Northwest Territories'), ('NU', 'Nunavut')], max_length=2)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('province', models.CharField(choices=[('NL', 'Newfoundland and Labrador'), ('PE', 'Prince Edward Island'), ('NS', 'Nova Scotia'), ('NB', 'New Brunswick'), ('QC', 'Quebec'), ('ON', 'Ontario'), ('MB', 'Manitoba'), ('SK', 'Saskatchewan'), ('AB', 'Alberta'), ('BC', 'British Columbia'), ('YT', 'Yukon'), ('NT', 'Northwest Territories'), ('NU', 'Nunavut')], max_length=2)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_type', models.CharField(choices=[('W', 'Weak'), ('P', 'Possible'), ('S', 'Strong')], max_length=1)),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.notice')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.record')),
            ],
        ),
    ]
