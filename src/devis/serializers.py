from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Categories, Services, Features, Projects


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'created_at', 'updated_at']


class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class FeaturesSerializer(ModelSerializer):
    class Meta:
        model = Features
        fields = '__all__'


class ProjectsSerializer(ModelSerializer):
    # services = serializers.RelatedField(many=True)
    service = ServicesSerializer(many=True)

    class Meta:
        model = Projects
        fields = '__all__'


class SendDevisMailSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=None, min_length=None, trim_whitespace=True, allow_blank=True)
    last_name = serializers.CharField(max_length=None, min_length=None, trim_whitespace=True, allow_blank=True)
    email = serializers.EmailField()
    contact = serializers.CharField(max_length=None, min_length=None, trim_whitespace=True, allow_blank=True)
    company_name = serializers.CharField(required=False, max_length=None, min_length=None, trim_whitespace=True,
                                         allow_blank=True)
    address = serializers.CharField(max_length=None, min_length=None, trim_whitespace=True, allow_blank=True)
    budget = serializers.IntegerField(required=False)
    delay = serializers.DateField()
    project_description = serializers.CharField(max_length=None, min_length=None, trim_whitespace=True,
                                                allow_blank=True, required=False)
    services = serializers.ListField(child=serializers.IntegerField())


class SendContactUsSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=None, required=True)
    email = serializers.EmailField(required=True)
    message = serializers.CharField(max_length=None, required=True)


class SubscribeToNewsLetter(serializers.Serializer):
    email = serializers.EmailField(required=True)

# class AdminGetDevisDemand(SendDevisMailSerializer):
#     project_state = serializers.CharField()
#     cost = serializers.DecimalField(max_digits=10, decimal_places=3)
#     request_state = serializers.IntegerField()
