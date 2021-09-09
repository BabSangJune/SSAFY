from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Stuff
from .forms import StuffForm

# Create your views here.
@require_safe
def index(request):
    return render(request, 'stuffs/index.html',)

@require_http_methods(['GET', 'POST'])
def board(request):
    stuffs = Stuff.objects.order_by('-pk')
    context = {
        'stuffs': stuffs,
    }
    return render(request, 'stuffs/board.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = StuffForm(request.POST, request.FILES)
        if form.is_valid():
            stuff = form.save()
            return redirect('stuffs:detail', stuff.pk)
    else:
        form = StuffForm()
    context = {
        'form': form,
    }
    return render(request, 'stuffs/create.html', context)

@require_safe
def detail(request, pk):
    stuff = get_object_or_404(Stuff, pk=pk)
    context = {
        'stuff': stuff,
    }
    return render(request, 'stuffs/detail.html', context)

@require_POST
def delete(request, pk):
    stuff = get_object_or_404(Stuff, pk=pk)
    stuff.delete()
    return redirect('stuffs:board')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    stuff = get_object_or_404(Stuff, pk=pk)
    if request.method == 'POST':
        form = StuffForm(request.POST, request.FILES, instance=stuff)
        if form.is_valid():
            form.save()
            return redirect('stuffs:detail', stuff.pk)
    else:
        form = StuffForm(instance=stuff)
    context = {
        'stuff': stuff,
        'form': form,
    }
    return render(request, 'stuffs/update.html', context)
    
    
    