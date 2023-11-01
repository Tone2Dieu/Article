from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
# Create your models here.

User = get_user_model()


class Article(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Titre')
    slug = models.SlugField(blank=True, unique=True, max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Autheur")
    date_created = models.DateField(blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False, verbose_name="publié")
    content = models.TextField(verbose_name="contenue")
    image = models.ImageField(blank=True, upload_to='blog')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            
        super().save(*args, **kwargs)

    def publier(self):
        if not self.author:
            return "cette article n'est pas encore été publier"
        return f"cette article a été publier pas {self.author.username} le {self.date_created}"



