# Generated by Django 3.1.4 on 2021-01-06 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='city',
            name='Provision',
        ),
        migrations.RemoveField(
            model_name='city',
            name='Timezone',
        ),
        migrations.RemoveField(
            model_name='city',
            name='published_date',
        ),
        migrations.AddField(
            model_name='city',
            name='Province',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
