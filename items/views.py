from django.shortcuts import render


def products(request):
    return render(request, 'products.html')


def faq(request):
    return render(request, 'faq.html')


def about(request):
    return render(request, 'about.html')
