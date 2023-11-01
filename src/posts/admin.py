from django.contrib import admin
from . import models
# Register your models here.


class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'published', 'date_created', 'date_updated')
    list_editable = ('published',)

admin.site.register(models.Article, AdminArticle)