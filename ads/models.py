from django.db import models
from django.utils import timezone

class AdPlacement(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    placement = models.ForeignKey(AdPlacement, on_delete=models.CASCADE, related_name='ads')
    code = models.TextField()
    active = models.BooleanField(default=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)

    def is_active(self):
        now = timezone.now().date()
        return self.active and (self.start_date <= now) and (self.end_date is None or self.end_date >= now)

    def __str__(self):
        return f"Ad for {self.placement.name}"
