from django.apps import AppConfig


class SitewebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'siteweb'

    def ready(self):
        import os
        from django.contrib.auth.models import User

        username = "admin"
        password = "admin12345"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email="admin@gmail.com",
                password=password
            )
