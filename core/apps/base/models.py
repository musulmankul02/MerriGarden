from django.db import models
from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField
# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = ' Название'
    )
    descriptions = RichTextField(
        verbose_name = 'Описание'
    )
    logo = models.ImageField(
        upload_to='logo_image',
        verbose_name='Логотип'
    )
    locations = models.CharField(
        max_length = 255,
        verbose_name = 'Адрес'
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )
    email = models.EmailField(
        verbose_name = 'Почта'
    )
    instagram = models.URLField(
        verbose_name = 'Инстаграм'
    )
    twitter = models.URLField(
        verbose_name = 'Вотсап'
    )
    facebook = models.URLField(
        verbose_name = 'Фейсбук'
    )
    class Meta:
        verbose_name = 'Основная настройка'
        verbose_name_plural = 'Основные настройки'



class Slide(models.Model):
    image = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to = 'slide/',
        verbose_name='Фотография',
        blank =True, null=True
    )
    title = RichTextField(
        verbose_name = 'Название'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Слайд на главной странице'
        verbose_name_plural = "Слайды на главной странице"

class Video(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='video/',
        verbose_name="Фотография для баннера",
        blank = True, null = True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название видео",
        blank=True,null=True
    )
    url = models.URLField(
        verbose_name="Ссылка на видео",
        blank=True,null=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Видео о MerriGarden"
        verbose_name_plural = "Видео о MerriGarden"



            