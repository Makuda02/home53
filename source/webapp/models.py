from django.db import models

status_choice = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Task(models.Model):
    description = models.CharField(max_length=60, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=40, choices=status_choice, verbose_name='Статус')
    data_of_complited = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    end_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    detailed_description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Подробное описание')


    def __str__(self):
        return f'{self.pk}. {self.description}'