from django.shortcuts import render
from imagegallery.models import Image, Location, Category


def index(request):
    images = Image.objects.all()
    context = {
        'images': images
    }
    return render(request, 'pages/index.html', context)
