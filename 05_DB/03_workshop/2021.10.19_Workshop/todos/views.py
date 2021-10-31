from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

# Create your views here.
@require_safe
def index(request):
    todos = Todo.objects.order_by('-pk')
    
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:index', todo.pk)
            
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/new.html', context)

