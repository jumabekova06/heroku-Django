from django.shortcuts import render

def my_main_page(request):
    return render(request, 'index.html')