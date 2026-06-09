from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from dateutil.relativedelta import relativedelta
import uuid

from django.conf import settings

class LinkTable(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    original_link = models.URLField(max_length=2048)
    short_link = models.CharField(max_length=20, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    click_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)


    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_links",
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + relativedelta(months=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_link} -> {self.original_link}"

    class Meta:
        ordering = ["-created_at"]
        
class ShortCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    short_code = models.CharField(max_length=20, unique=True, db_index=True)
        

#This is used to store a hash map of the alphanumeric characters
class LookUpTable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # to map PostgreSQL JSONB data type directly
    hash_matrix = models.JSONField()
    
    def save(self, *args, **kwargs):

        current_time = timezone.now()
        month_upper = current_time.strftime('%B').upper()
        self.name = f"{current_time.strftime('%Y')}-{month_upper}-{current_time.strftime('%d')}"
        
        super().save(*args, **kwargs)

        
