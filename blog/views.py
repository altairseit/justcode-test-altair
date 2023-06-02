from django.shortcuts import render
from .models import AboutUs

def about_view(request):
    about_us = AboutUs.objects.first()

    context = {
        'about_us': about_us,
    }

    return render(request, 'about.html', context)
