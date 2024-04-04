from django.db import models
from django.db.models import Prefetch


class Section(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название секции для меню')
    link = models.TextField(verbose_name='Ссылка для определенной секции', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'


class Menu(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название меню')
    sections = models.ManyToManyField(Section, verbose_name='Название секций', related_name='menus')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
