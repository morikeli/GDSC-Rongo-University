from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import User, CoreTeam, TechTeam, Sessions
import uuid


@receiver(pre_save, sender=User)
def generate_userID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '').upper()[:20]

