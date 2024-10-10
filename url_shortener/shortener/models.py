# models.py
import uuid
import string
from django.db import models
from django.contrib.auth.models import User

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.original_url} -> {self.short_url}"

    # Convert UUID to Base62
    def base62_encode(self, num):
        chars = string.ascii_letters + string.digits  # Base62: a-z, A-Z, 0-9
        base = len(chars)
        encoded = []
        while num > 0:
            num, rem = divmod(num, base)
            encoded.append(chars[rem])
        return ''.join(encoded[::-1])

    # Generate a short URL using Base62 conversion of UUID
    def save(self, *args, **kwargs):
        if not self.short_url:
            uuid_int = self.uuid.int  # Get the integer representation of the UUID
            self.short_url = self.base62_encode(uuid_int)[:6]  # Take only the first 6 characters for the short URL
        super().save(*args, **kwargs)
