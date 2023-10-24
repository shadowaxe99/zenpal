
from django.db import models
from apps.contact_management.models import Contact

class Interaction(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()

    class Meta:
        verbose_name = "Interaction"
        verbose_name_plural = "Interactions"

    def __str__(self):
        return f"{self.contact.name} - {self.date}"
