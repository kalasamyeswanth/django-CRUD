# Create your views here.
from django.shortcuts import render, redirect
from .models import Notemodel
from .forms import Noteform

def book_list(request):
    books = Notemodel.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = Noteform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = Noteform()
    return render(request, 'book_form.html', {'form': form})

def book_update(request, pk):
    book = Notemodel.objects.get(pk=pk)
    if request.method == 'POST':
        form = Noteform(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = Noteform(instance=book)
    return render(request, 'book_form.html', {'form': form})

def book_delete(request, pk):
    book = Notemodel.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})
