from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    number = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )

    data = models.CharField(
        max_length = 255,
        verbose_name = 'Дата'
    )
   

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Запрос на связь'
        verbose_name_plural = 'Запросы на связь'


class PageContact(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    email = models.EmailField(
        verbose_name = 'Дата',
    )
    number = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )
    subject = models.CharField(
        max_length =255,
        verbose_name = 'Тема',
    )
    message = models.TextField(
        verbose_name = 'Сообщение',
    )
    


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Соощении'

