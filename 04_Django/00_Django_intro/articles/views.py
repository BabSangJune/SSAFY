
import random
from django.shortcuts import render

# Create your views here.
def index(request): #첫번째 인자는 반드시 request (해당 이름이 아니어도 되지만 권장사항)
    return render(request, 'articles/index.html') # render 첫번째 인자는 request, 


def greeting(request):
    foods = ['곰국', '김고추장', '장조림', '라면']
    info = {
        'name': '양밥',
        'hobby': '빠삐꼬 눈에 보이면 가져다 버리기',
    }

    context = {
        'foods': foods,
        'info': info,
    }

    return render(request, 'articles/hello.html', context)


def dinner(request):
    foods = ['피자', '치킨', '족발', '햄버거', '초밥']
    pick = random.choice(foods) #random 함수 사용 하나 뽑기
    context = {
        'foods': foods,
        'pick': pick,
    }

    return render(request, 'articles/dinner.html', context)


def dtl_practice(request):
    foods = ['피자', '치킨', '족발', '햄버거', '초밥']
    fruits = ['mango', 'hard-peach', 'saturn-peach', 'apple']
    user_list = []
    
    context = {
        'foods': foods,
        'fruits': fruits,
        'user_list': user_list,
    }

    return render(request, 'articles/dtl_practice.html', context)


def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')

    context = {
        'message': message,
    }

    return render(request, 'articles/catch.html', context)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/hello2.html', context)