from importlib import import_module

from django.apps import AppConfig
from django.conf import settings
from django.conf.urls.static import static


class DjangoSOSConfig(AppConfig):
    name = 'django_sos'

    def ready(self):
        if settings.DEBUG and settings.MEDIA_ROOT:
            import_module(settings.ROOT_URLCONF).urlpatterns.extend(static(
                settings.MEDIA_URL,
                document_root=settings.MEDIA_ROOT,
            ))
