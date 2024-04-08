from django.contrib import admin
from apps.secondary import models

# Register your models here.

class NewsFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )

class UslugaFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name','descriptions' )
    search_fields = ('name', 'descriptions')


class TeamFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )

  
class BossFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name',)
    search_fields = ('name', )

class TeamAboutFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name',)
    search_fields = ('name', )

admin.site.register(models.Condition)
admin.site.register(models.Gallery)
admin.site.register(models.List)
admin.site.register(models.TeamAbout, TeamAboutFilterAdmin)
admin.site.register(models.Boss, BossFilterAdmin)
admin.site.register(models.Team, TeamFilterAdmin)
admin.site.register(models.Usluga, UslugaFilterAdmin)
admin.site.register(models.News, NewsFilterAdmin)
