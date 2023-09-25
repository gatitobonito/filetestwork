from django.db import models

from .serializers import FileSerializer


class File(models.Model):
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField()

    def get_serializer_class(self):
        return FileSerializer

    def __str__(self):
        return self.name
