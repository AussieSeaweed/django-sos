import os
from uuid import uuid4

from django.db.models import Model
from django.utils.deconstruct import deconstructible


@deconstructible
class UploadHexTo:
    def __init__(self, path: str) -> None:
        self.path: str = path

    def __call__(self, instance: Model, filename: str) -> str:
        ext = filename.split('.')[-1]

        return os.path.join(self.path, f'{uuid4().hex}.{ext}')
