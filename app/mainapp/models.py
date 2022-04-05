from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    support_email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " (org)"

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    dpa_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    pending = models.BooleanField(default=True)

    def __str__(self):
        return self.name + " (vend)"

class Stakeholder(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " (stak)"
