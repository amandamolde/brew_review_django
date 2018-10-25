from django.db import models

# Create your models here.

class Brewery(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    description = models.TextField(blank=True)
    website_url = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE, related_name='reviews')
    atmosphere = models.PositiveIntegerField()
    beer_tenders = models.PositiveIntegerField()
    beer_selection = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    photo = models.TextField(blank=True)

    def __str__(self):
        return self.notes