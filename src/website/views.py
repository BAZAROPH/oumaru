from django.shortcuts import render


# Create your views here.

def page_not_found(request, *args, **kwargs):
    return render(request, '404.html')


def server_error(request, *args, **kwargs):
    return render(request, '500.html')


def homeView(request):
    return render(request, 'pages/home.html')


def contactUsView(request):
    return render(request, 'pages/contact-us.html')


def aboutUsView(request):
    return render(request, 'pages/about-us.html')


def servicesView(request):
    return render(request, 'pages/services.html')


def devisHomeView(request):
    return render(request, 'devis/index.html')


def clientDevisRequestView(request):
    return render(request, 'notification.html')