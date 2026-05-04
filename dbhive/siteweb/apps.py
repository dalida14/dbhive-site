from django.apps import AppConfig


class SitewebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'siteweb'

    def ready(self):
        import os
        from django.db.utils import OperationalError

        try:
            from django.contrib.auth.models import User

            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="admin",
                    email="admin@gmail.com",
                    password="admin12345"
                )

        except OperationalError:
            # La base n'est pas encore prête → on ignore
            pass
