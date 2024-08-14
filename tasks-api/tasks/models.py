from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Task(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название'
    )
    description = models.CharField(
        max_length=500,
        blank=True,
        verbose_name='Описание',
    )
    is_done = models.BooleanField(
        default=False,
        verbose_name='Выполнена'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        verbose_name='Владелец'
    )

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'Задача "{self.name}" пользователя {self.owner.email}'
    