from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    important = models.BooleanField(default=False, verbose_name='Важное')
    completed = models.BooleanField(default=False, verbose_name='Выполнено')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['completed']

    def __str__(self):
        return self.title

