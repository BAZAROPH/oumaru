from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Libellé")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Date de suppression")

    class Meta:
        verbose_name = 'Catégorie'

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name="Nom")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Prix")
    delay = models.CharField(max_length=255, blank=False, null=False, verbose_name="Délai de livraison")
    image = CloudinaryField('image', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Date de suppression")

    category = models.ManyToManyField(Categories)

    class Meta:
        verbose_name = "Service"

    def __str__(self):
        return self.name


class Features(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Nom")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, verbose_name="Prix")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière modidification")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Date de suppression")

    service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name="Service")

    class Meta:
        verbose_name = "Fonctionnalité"

    def __str__(self):
        return self.name


class Projects(models.Model):
    REQUEST_STATES = (
        (0, 'En attente'),
        (1, 'Validé'),
        (2, 'Supprimé')
    )
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Prénom")
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nom")
    contact = models.CharField(max_length=255, null=True, blank=True, verbose_name="Contact")
    email = models.EmailField(null=True, blank=True, verbose_name="email")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Adresse")
    project_state = models.CharField(max_length=255, null=False, default='Devis')
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=True, verbose_name="Coût")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    delay = models.DateField(null=False, verbose_name="Délai de livraison")
    request_state = models.IntegerField(choices=REQUEST_STATES, default=0, verbose_name="Statut de la requête")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Date de suppression")

    service = models.ManyToManyField(Services)

    class Meta:
        verbose_name = "Projet"


class NewsLetter(models.Model):
    email = models.EmailField(verbose_name='Email', blank=True, null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Date de suppression")
