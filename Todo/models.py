from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class UserRegistration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_fullname = models.TextField()
    user_email = models.EmailField(unique=True)
    password = models.TextField()
    created_at = models.DateTimeField(default=timezone.now) 
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    EMAIL_FIELD = 'user_email'  # <-- recommended
    USERNAME_FIELD = 'user_email'  # <-- optional if you do login with email

    def get_email_field_name(self):
        return 'user_email'


    def __str__(self):
        return self.user_email


