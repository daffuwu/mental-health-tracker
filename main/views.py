from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2306152235',
        'name': 'Daffa Rayhan Ananda',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)