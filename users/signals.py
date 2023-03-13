from django.db.models.signals import pre_save, post_save
from .models import CoreTeam, TechTeam, Sessions
from django.dispatch import receiver
import uuid

@receiver(pre_save, sender=CoreTeam)
def generate_coreteamID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '').upper()[:20]

@receiver(pre_save, sender=TechTeam)
def generate_techteamID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '').upper()[:20]

@receiver(pre_save, sender=Sessions)
def generate_sessionsID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '').upper()[:20]

