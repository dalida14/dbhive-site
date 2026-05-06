from django.db import models
from django.urls import reverse


class Article(models.Model):
    class Categorie(models.TextChoices):
        INFORMATIQUE = "informatique", "Informatique"
        ELECTRONIQUE = "electronique", "Électronique"
        ELECTROMENAGER = "electromenager", "Électroménager"
        PRODUITS_CHIMIQUES = "produits_chimiques", "Produits chimiques"
        AUTRES = "autres", "Autres"

    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    contenu = models.TextField()
    image = models.ImageField(upload_to="articles/")
    categorie = models.CharField(max_length=32, choices=Categorie.choices)
    date_publication = models.DateTimeField(auto_now_add=True)
    publie = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["-date_publication"]

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})