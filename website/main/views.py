from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def products(request):
    return render(request, 'main/products.html')


def white_tshirt(request):
    return render(request, 'main/clothes/white_tshirt.html')


def black_tshirt(request):
    return render(request, 'main/clothes/black_tshirt.html')


def white_hoodie(request):
    return render(request, 'main/clothes/white_hoodie.html')


def black_hoodie(request):
    return render(request, 'main/clothes/black_hoodie.html')
