from django.db import models
from apps.company.models import company
class Video(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    company = models.ForeignKey(to=company, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='video/video/video/', verbose_name='Видео')
    when  = models.DateField(verbose_name='Когда')
    description = models.TextField(verbose_name='Описание')

    def __str__(self) -> str:
        return self.when
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видосы'