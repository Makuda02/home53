# Generated by Django 4.2.7 on 2023-12-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_task_detailed_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='summary',
            field=models.CharField(default=1996, max_length=60, verbose_name='Краткое описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.CharField(choices=[('Task', 'Задача'), ('Bug', 'Ошибка'), ('Enhancement', 'Улучшение')], default=1996, max_length=60, verbose_name='Тип'),
            preserve_default=False,
        ),
    ]
