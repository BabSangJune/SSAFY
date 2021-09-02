import articles
from .models import Article
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    #가져와서 뒤집기
    # articles = Article.objects.all()[::-1]
    # 뒤집어서 가져오기
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article(title=title, content=content)
    article.save()

    return render(request, 'articles/index.html')



def detail(request, pk):
    pass


def delete(request, pk):
    pass


def edit(request, pk):
    pass


def update(request, pk):
    pass
