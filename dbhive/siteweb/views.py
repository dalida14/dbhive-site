from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.encoding import iri_to_uri

from .models import Article
from .forms import QuoteRequestForm


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def logistics(request):
    articles = Article.objects.filter(publie=True).order_by("-date_publication")
    categories = Article.Categorie.choices
    return render(
        request,
        "logistics.html",
        {
            "articles": articles,
            "categories": categories,
        },
    )


def quote(request):
    article_param = request.GET.get("article") or ""

    article_obj = None
    if article_param:
        article_obj = Article.objects.filter(slug=article_param, publie=True).only("titre").first()

    article_display_name = article_obj.titre if article_obj else article_param

    categories = Article.Categorie.choices

    initial_description = ""
    if article_display_name:
        initial_description = f"Demande de devis pour : {article_display_name}"

    if request.method == "POST":
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            structure = form.cleaned_data["structure"]
            contact = form.cleaned_data["contact"]
            email = form.cleaned_data["email"]
            telephone = form.cleaned_data["telephone"]
            message_client = form.cleaned_data["description"]
            article_post = form.cleaned_data.get("article") or ""

            article_post_obj = None
            if article_post:
                article_post_obj = (
                    Article.objects.filter(slug=article_post, publie=True).only("titre").first()
                )
            article_name_for_email = (
                article_post_obj.titre if article_post_obj else (article_post or "Aucun")
            )

            recipients = [email for _, email in getattr(settings, "ADMINS", [])]
            if not recipients:
                fallback_admin = getattr(settings, "DEFAULT_FROM_EMAIL", "")
                if fallback_admin:
                    recipients = [fallback_admin]

            send_mail(
                subject="Nouvelle demande de devis",
                message=(
                    "Nouvelle demande de devis\n\n"
                    f"Nom du client : {contact} ({structure})\n"
                    f"Email : {email}\n"
                    f"Téléphone : {telephone or '-'}\n"
                    f"Article concerné : {article_name_for_email}\n\n"
                    "Message :\n"
                    f"{message_client}\n"
                ),
                from_email=getattr(settings, "DEFAULT_FROM_EMAIL", None),
                recipient_list=recipients,
                fail_silently=False,
            )

            messages.success(request, "Votre demande a été envoyée avec succès")
            return redirect("quote")
    else:
        form = QuoteRequestForm(
            initial={
                "description": initial_description,
                "article": article_param,
                "domaine": "articles" if article_display_name else "",
            }
        )

    return render(
        request,
        "quote.html",
        {
            "article_param": iri_to_uri(article_param),
            "article_display_name": article_display_name,
            "initial_description": initial_description,
            "categories": categories,
            "form": form,
        },
    )


def contact(request):
    return render(request, "contact.html")


def articles(request):
    # Alias: même page que /logistique/ (ne change pas le design existant)
    return logistics(request)


def article_detail(request, slug: str):
    article = get_object_or_404(Article, slug=slug, publie=True)
    return render(request, "article_detail.html", {"article": article})

