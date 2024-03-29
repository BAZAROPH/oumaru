"""oumaru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from devis.views import (CategoriesViewSet, ServicesViewSet, FeaturesViewSet, ProjectsViewSet, SendDevisMailView,
                         sendContactUsView, newsLetterView
                         )

router = routers.SimpleRouter()
router.register('categories', CategoriesViewSet, basename='categories')
router.register('services', ServicesViewSet, basename='services')
router.register('features', FeaturesViewSet, basename='features')
router.register('projects', ProjectsViewSet, basename='projects')
# router.register('sendmail', SendMailView, basename='sendmail')

urlpatterns = [
    path('root/', admin.site.urls),
    path('', include('website.urls')),
    path('api/send-devis-mail', SendDevisMailView.as_view()),
    path('api/send-contact-us-mail', sendContactUsView.as_view()),
    path('api/subscribe/newsletter', newsLetterView.as_view()),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
