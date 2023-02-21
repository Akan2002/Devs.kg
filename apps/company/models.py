from django.db import models

class company(models.Model):
    logo = models.ImageField(upload_to='company/logos/', verbose_name='Логотип компании')
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    telegram = models.URLField(verbose_name='Телеграмм')
    whatsapp = models.URLField(verbose_name='Вотсапп')

    @property
    def vakanci_amount(self):
        return self.Vakancies.count()

    @property
    def video_amount(self):
        return self.videos.count()
    @property
    def merop_amount(self):
        return self.merops.count()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
