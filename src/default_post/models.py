from django.db import models


class DefaultPost(models.Model):
    title = models.CharField(verbose_name='Название поста', max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name='Текст поста', null=False, blank=False)

    class Meta:
        verbose_name = 'Стандартный пост'
        verbose_name_plural = 'Стандартные посты'

    def __str__(self):
        return self.title
