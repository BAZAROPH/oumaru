from django.contrib import admin
from .models import Categories, Services, Features, Projects


# Register your models here.

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
        "updated_at",
        "deleted_at",
    )
    empty_value_display = "Vide"


@admin.register(Services)
class ServicesAmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "delay",
        "created_at",
        "updated_at",
        "deleted_at",
    )

    empty_value_display = "Vide"


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "created_at",
        "updated_at",
        "deleted_at",
    )

    empty_value_display = "Vide"


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = (
        "request_state",
        "first_name",
        "last_name",
        "contact",
        "email",
        "address",
        "project_state",
        "cost",
        "description",
        "delay",
        "created_at",
        "updated_at",
        "deleted_at",
    )

    empty_value_display = "Vide"
