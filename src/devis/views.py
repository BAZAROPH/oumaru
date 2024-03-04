import statistics
from pprint import pprint

from django.shortcuts import render
from django.core.mail import send_mail
from django.template import loader
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import (CategoriesSerializer, ServicesSerializer, FeaturesSerializer, ProjectsSerializer,
                          SendDevisMailSerializer, SendContactUsSerializer,
                          SubscribeToNewsLetter
                          )
from .models import Categories, Services, Features, Projects, NewsLetter


# Create your views here.
class CategoriesViewSet(ReadOnlyModelViewSet):
    serializer_class = CategoriesSerializer

    def get_queryset(self):
        query_set = Categories.objects.all()
        return query_set


class ServicesViewSet(ReadOnlyModelViewSet):
    serializer_class = ServicesSerializer

    def get_queryset(self):
        query_set = Services.objects.all()
        return query_set


class FeaturesViewSet(ReadOnlyModelViewSet):
    serializer_class = FeaturesSerializer

    def get_queryset(self):
        query_set = Features.objects.all()
        return query_set


class ProjectsViewSet(ReadOnlyModelViewSet):
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_paginated_response(self, data):
        return Response(data)

    def get_queryset(self):
        query_set = Projects.objects.all()
        return query_set


class SendDevisMailView(APIView):
    def post(self, request, format=None):
        serializer = SendDevisMailSerializer(data=request.data)
        # check if data is valid
        if serializer.is_valid():
            # Save data
            data = serializer.data
            project = Projects(
                description=data['project_description'],
                delay=data['delay'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                contact=data['contact'],
                email=data['email'],
                address=data['address'],
            )
            project.save()
            project.service.set(data['services'])

            # generate email html page
            html_message = loader.render_to_string('clientDevisRequest.html', {
                'last_name': data['last_name'],
                'first_name': data['first_name']
            })
            send_mail('Demande de devis', 'Ce message est automatique, veuillez ne pas répondre',
                      from_email='Oumaru <no-reply@oumaru.com>', recipient_list=[data['email']],
                      fail_silently=False, html_message=html_message)

            html_message = loader.render_to_string('notification.html', {
                'title': 'Vous avez une nouvelle demande de devis',
                'client': f"{data['last_name']} {data['first_name']}",
                'message': data['project_description'],
            })
            send_mail('Message', 'Ce message est automatique, veuillez ne pas répondre',
                      from_email='Oumaru <no-reply@oumaru.com>', recipient_list=['message@oumaru.com'],
                      fail_silently=False, html_message=html_message)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class sendContactUsView(APIView):
    def post(self, request, format=None):
        serializer = SendContactUsSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            html_message = loader.render_to_string('contacUsEmail.html', {
                'full_name': data['full_name']
            })
            send_mail('Question', 'Ce message est automatique, veuillez ne pas répondre',
                      from_email='Oumaru <no-reply@oumaru.com>', recipient_list=[data['email']],
                      fail_silently=False, html_message=html_message)

            html_message = loader.render_to_string('notification.html', {
                'title': 'Vous avez un nouveau message',
                'client': data['full_name'],
                'message': data['message']
            })
            send_mail('Message', 'Ce message est automatique, veuillez ne pas répondre',
                      from_email='Oumaru <no-reply@oumaru.com>', recipient_list=['message@oumaru.com'],
                      fail_silently=False, html_message=html_message)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class newsLetterView(APIView):
    def post(self, request, format=None):
        serializer = SubscribeToNewsLetter(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            if NewsLetter.objects.filter(email=data['email']).exists():
                pass
            else:
                NewsLetter.objects.create(email=data['email'])
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

# class AdminGetDevisDemandView(APIView):
#     def get(self, request):
#         projects = Projects.objects.all()
