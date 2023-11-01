from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views import generic
from . import models
from django.urls import reverse_lazy
# Create your views here.





def home(request):
    return render(request, 'blog/index.html', {"date": datetime.today()})


class ArticleList(generic.ListView):
    model = models.Article
    template_name = 'blog/articles.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = models.Article.objects.filter(published=True)
        return queryset


class MyArticle(generic.DetailView):
    model = models.Article
    template_name = 'blog/my-article.html'
    context_object_name = 'post'


class UpdateArticle(generic.UpdateView):
    model = models.Article
    template_name = 'blog/update_new-article.html'
    context_object_name = 'post'
    success_url = reverse_lazy('articles')
    fields = [
        "title",
        "published",
        "image",
        "content"
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit"] = "Modifier"
        return context

class DeleteArticle(generic.DeleteView):
    model = models.Article
    template_name = 'blog/delete-article.html'
    context_object_name = 'post'
    success_url = reverse_lazy('articles')


class NewArticle(generic.CreateView):
    model = models.Article
    template_name = 'blog/update_new-article.html'
    success_url = reverse_lazy('articles')
    fields = [
        "title",
        "author",
        "date_created",
        "published",
        "content"
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit"] = "Enregistrer"
        return context
