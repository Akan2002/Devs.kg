from django.db import models
from apps.company.models import company
class Vakanci(models.Model):
    name = models.CharField(max_length=120, verbose_name='Нахвание')
    company = models.ForeignKey(to=company, on_delete=models.CASCADE, related_name='Vakancies')
    job_title = models.CharField(max_length=120, verbose_name='Должность')
    salary = models.CharField(max_length=200, verbose_name='Оклад')
    type = models.CharField(max_length=127, verbose_name='Тип')
    description = models.TextField(verbose_name='Описание')
    email = models.EmailField(verbose_name='Емаил')
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Ваканксия'
        verbose_name_plural = 'Вакансии'