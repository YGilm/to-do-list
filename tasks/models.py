from django.db import models

from users.models import User


class Task(models.Model):
    """
    Модель задачи.
    """
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    status = models.BooleanField(default=False, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменена')
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['user']

    def __str__(self):
        return self.title
