# Generated by Django 3.2.16 on 2024-04-18 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_auto_20240403_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Локация', 'verbose_name_plural': 'Локации'},
        ),
        migrations.AddField(
            model_name='location',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
