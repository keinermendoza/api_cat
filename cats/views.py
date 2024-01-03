from django.shortcuts import render
from django.urls import reverse
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site

from .models import Cat
from .utils import put_text_on_image
from django.views.decorators.http import require_GET, require_POST

def home(request):
    
    return render(request, 'cats/home.html')

@require_GET
def api_random_cat(request):    
    cat = Cat.get_random_cat()
    image = cat.url

    text = request.GET.get('text')
    if text:
        image = put_text_on_image(cat.url, text=text)


    image_full_url = f'http://{get_current_site(request).domain}/{image}'

    return JsonResponse({'url': image_full_url})
