
from django.db import models
from django.contrib.auth.models import User

class Email(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_to = models.EmailField()
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
