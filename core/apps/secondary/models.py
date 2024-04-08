from django.db import models
from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField



# Create your models here.
class Condition(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок'
    )
    descriptions = RichTextField(
        verbose_name = "Описание"
    )
    image1 = models.ImageField(
        upload_to='image1/',
        verbose_name='Фотографии'
    )
    image2 = models.ImageField(
        upload_to='image2/',
        verbose_name='Фотографии'
    )
    class Meta:
        verbose_name = 'Условие '
        verbose_name_plural = 'Условия'




class News(models.Model):
    name = models.CharField(
        max_length =255,
        verbose_name = 'Название'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фотография'
    )
    descriptions1 = RichTextField(
        verbose_name = 'Описание1'
    )
    letter = models.TextField(
        verbose_name = 'Письмо текст'
    )
    descriptions2 = RichTextField(
        verbose_name = 'Описание1'
    )
    
    def __str__(self):
        return self.letter
   
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Usluga(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Название_услуги'
    )
    descriptions = RichTextField(
        verbose_name = "Описание_услуги"
    )
    image = models.ImageField(
        upload_to='image_usluga',
        verbose_name='Фотграфия_услуги'
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Boss(models.Model):
    name = models.CharField(
        max_length = 255,
         verbose_name = 'Имя_боса'
    )
    image_boss = models.ImageField(
        upload_to='image_boss/',
        verbose_name = "Фото боса"
    )
    about_boss = RichTextField(
        verbose_name = 'Информация про боса'
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Босс'
        verbose_name_plural = 'Босс'

class Team(models.Model):
    image = models.ImageField(
        upload_to='image_team/',
        verbose_name = "Фото мемберов"
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class TeamAbout(models.Model):
    image = models.ImageField(
        upload_to='image_team/',
        verbose_name='Фото Команды'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    work = models.CharField(
        max_length = 255,
        verbose_name = 'Должность'
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
    email = models.EmailField(
        verbose_name = 'Почта'
    )
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Член команды'
        verbose_name_plural = 'Члены команды'

class List(models.Model):
    image_one = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='price/',
        verbose_name="Первая фотография",
        blank = True, null = True
    )
    image_two = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='price/',
        verbose_name="Первая фотография",
        blank = True, null = True
    )
    image = models.ImageField(
        upload_to='image',
        verbose_name='Фото Граунд'
    )

    class Meta:
            verbose_name = "Прайс"
            verbose_name_plural = "Прайс"


class Gallery(models.Model):
    image = models.ImageField(
        upload_to='image_gallery',
        verbose_name='Фотография'
    )
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'
        
 

