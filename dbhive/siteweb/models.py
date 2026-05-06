from django.db import models
from django.utils.text import slugify

class Article(models.Model):

    class Categorie(models.TextChoices):
        LOGISTIQUE = "logistique", "Logistique"
        TRANSPORT = "transport", "Transport"

    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)

    slug = models.SlugField(unique=True, blank=True)
    publie = models.BooleanField(default=True)
    categorie = models.CharField(max_length=50, choices=Categorie.choices, default=Categorie.LOGISTIQUE)
    date_publication = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre
