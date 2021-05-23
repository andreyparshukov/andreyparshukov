# Generated by Django 3.0.7 on 2020-08-26 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='lang',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('rus', 'russian')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='settinglang',
            name='lang',
            field=models.CharField(choices=[('en', 'English'), ('rus', 'russian')], max_length=6),
        ),
    ]
