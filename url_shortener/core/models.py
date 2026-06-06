from django.db import models
from django.contrib.auth.models import User
import uuid

from django.conf import settings

class LookUpTable(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    original_link = models.URLField(max_length=2048)
    short_code = models.CharField(max_length=20, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    click_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)


    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_links"
    )

    def save(self, *args, **kwargs):
        if not self.expires_at:
            from django.utils import timezone
            from dateutil.relativedelta import relativedelta
            self.expires_at = timezone.now() + relativedelta(months=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} -> {self.original_link}"

    class Meta:
        ordering = ["-created_at"]