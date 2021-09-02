import articles
from .models import Article

from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    #가져와서 내가 뒤집은거
    # articles = Article.objects.all()[::-1]
    #뒤집어서 가져온거
    articles = Article.objects.order_by('-pk')
    print(articles)
    
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    #등록하는 방법 3가지

    article = Article(title=title, content=content)
    article.save()
    
    #게시글 조회 x URL이 create에 머물고 있음
    # return render(request, 'articles/index.html')

    # return redirect('/articles/')
    # return redirect('articles:index')

    # 글을 작성을 했으면 해당 글의 디테일 페이지로 이동하자
    return redirect('articles:detail', article.pk)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')

    article.save()

    return redirect('articles:detail', article.pk)
