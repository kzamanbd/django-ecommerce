# Generated by Django 3.2.9 on 2021-11-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeroSection', '0002_aboutus_contact_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='paragraph',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='title',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='paragraph',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='paragraph',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='services',
            name='paragraph',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]