from django.contrib import admin

# Register your models here.
from apps.video.models import(
    Video,
)
admin.site.register(Video)