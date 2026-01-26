from django.db import models


class SuccessStory(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='success_stories/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Vision(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='vision/')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CustomerExperience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='customer_experience/')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
