import re
import articles
from django.shortcuts import render, redirect, get_list_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe
from .models import Article
from .forms import ArticleForm


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')

    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }

    return render(request, 'articles/create.html', context)

def detail(request):
    return render(request, 'articles/detail.html',)

def delete(request, pk):
    pass
    return redirect('articles:index')

def update(request, pk):
    pass
    return render(request, 'articles/index.html',)
