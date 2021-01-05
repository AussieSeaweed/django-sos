from importlib import import_module

from django.apps import AppConfig
from django.conf import settings
from django.conf.urls.static import static


class DjangoSOSConfig(AppConfig):
    """DjangoSOSConfig is the class for the django-sos app configuration."""

    name: str = 'django_sos'

    def ready(self) -> None:
        """Automatically hosts media files during debugging.

        :return: None
        """
        if settings.DEBUG_SERVE_MEDIA and settings.DEBUG and settings.MEDIA_ROOT:
            import_module(settings.ROOT_URLCONF).urlpatterns.extend(static(
                settings.MEDIA_URL,
                document_root=settings.MEDIA_ROOT,
            ))
