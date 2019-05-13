from django.shortcuts import render
from .models import Image,Location


def index(request):
    images = Image.objects.all()
    context = {
        'images': images
    }
    return render(request, 'pages/index.html', context)


def search_results(request):
    locations = Location.objects.all()
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"Showing: {search_term} pictures"

        return render(request, 'pages/search.html', {"message": message, "images": searched_images, "locations":locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})

def specific_location(request, location):
    locations = Location.objects.all()
    location_results = Image.filter_location(location)
    return render(request, 'search.html', {"locations": locations, "images": location_results})
