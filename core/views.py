from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Note
from .forms import PostForm

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'core-templates/note_list.html', {"notes": notes})

def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'core-templates/note_details.html', {"note": note, "pk": pk})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_details', pk=form.save().pk)
    else:
        form = PostForm()
    return render(request, 'core-templates/post_edit.html', {"form": form})