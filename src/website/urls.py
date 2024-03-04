from django.urls import path
from .views import (homeView, contactUsView, aboutUsView, servicesView, devisHomeView, clientDevisRequestView)
from website.views import server_error
handler404 = 'website.views.page_not_found'
handler500 = 'website.views.server_error'

urlpatterns = [
    path('', homeView, name='home'),
    path('contact-us/', contactUsView, name='contact-us'),
    path('about-us/', aboutUsView, name='about-us'),
    path('services/', servicesView, name='services'),
    path('devis/', devisHomeView, name='devis-home'),
    path('devisR/', clientDevisRequestView, name='devis-r')
    # path('500/', server_error),
]