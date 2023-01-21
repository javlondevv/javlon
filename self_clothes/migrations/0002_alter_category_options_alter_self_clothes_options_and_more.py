# Generated by Django 4.1.3 on 2022-11-21 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_clothes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='self_clothes',
            options={'verbose_name_plural': 'Clothes'},
        ),
        migrations.AddField(
            model_name='self_clothes',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]