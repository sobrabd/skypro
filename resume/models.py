from django.db import models
from django.contrib.auth.models import User


class OwnedModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True


class Resume(OwnedModel):
    status = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    experience = models.TextField(max_length=255)
    portfolio = models.URLField(max_length=200)
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)

    def __repr__(self):
        return f"<Resume id: {self.id}>"
