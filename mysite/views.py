from django.shortcuts import render

def home(request):
    template_name = "halaman/index.html"
    context = {
        'title':'selamat datang di halaman home',
        'umur': 20,
    }
    return render(request, template_name, context)

def about(request):
    template_name = "about.html"
    context = {
        'title':'selamat datang di halaman about',
        'umur': 20,
    }
    return render(request, template_name, context)