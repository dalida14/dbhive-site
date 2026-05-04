from django.db import models
from django.utils.text import slugify


class Article(models.Model):

    class Categorie(models.TextChoices):
        INFORMATIQUE = "informatique", "Informatique"
        ELECTRONIQUE = "electronique", "Électronique"
        ELECTROMENAGER = "electromenager", "Électroménager"
        PRODUITS_CHIMIQUES = "produits_chimiques", "Produits chimiques"
        AUTRES = "autres", "Autres"

    titre = models.CharField(max_length=255)
    resume = models.CharField(max_length=255)
    contenu = models.TextField()
    image = models.ImageField(upload_to="articles/")
    categorie = models.CharField(max_length=32, choices=Categorie.choices)
    date_publication = models.DateTimeField(auto_now_add=True)
    publie = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titre)
            slug = base_slug
            counter = 1

            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre
