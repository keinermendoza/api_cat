from django.shortcuts import render
from .models import Cat
from .utils import put_text_on_image

def home(request):
    cat = Cat.get_random_cat()
    image_text = put_text_on_image(cat.url)
    return render(request, 'cats/home.html', {'image':image_text})