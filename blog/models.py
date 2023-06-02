from django.db import models

class AboutUs(models.Model):
    whatsapp_link = models.URLField()
    telegram_link = models.URLField()
    text = models.TextField()

    def __str__(self):
        return "About Us"