from django.db import models
from apps.company.models import company
class Event(models.Model):
    date = models.DateTimeField(verbose_name='Дата и время проведения')
    name = models.CharField(max_length=127, verbose_name='Название')
    location = models.CharField(max_length=127, verbose_name='Локация')
    image = models.ImageField(upload_to='merop/image/', verbose_name='Картинка')
    description  =models.TextField(verbose_name='Описание')
    company = models.ForeignKey(to=company, on_delete=models.CASCADE, related_name='merops', verbose_name='Компания')

    def __str__(self) -> str:
        return self.name
        
    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
