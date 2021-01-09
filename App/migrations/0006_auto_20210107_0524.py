# Generated by Django 3.1.4 on 2021-01-07 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20210106_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='point',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='subj',
            field=models.CharField(choices=[('Python', 'Python'), ('JQuery', 'JQuery'), ('JavaScript', 'JavaScript')], default='Python', max_length=10),
        ),
    ]
