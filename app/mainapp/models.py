from django.db import models

class organization(models.Model):
    name = models.CharField(max_length=100)
    password = models.PasswordField(max_length=100)
    support_email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " (org)"

class vendor(models.Model):
    name = models.CharField(max_length=100)
    dpa_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " (vend)"

class stakeholder(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " (stak)"
