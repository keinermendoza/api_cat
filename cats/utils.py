from random import randint
from os import path, listdir, remove
from django.conf import settings
from PIL import Image, ImageFont, ImageDraw

DEFAULT_FONT_SIZE = 60
LIMIT_TEMPORAL_IMAGES = 20
TEMPORAL_IMAGE_FOLDER = f'{settings.MEDIA_ROOT}/temporal'

def cheack_temporal_folder():
    temporal_images_folder = listdir(TEMPORAL_IMAGE_FOLDER)

    if LIMIT_TEMPORAL_IMAGES < len(temporal_images_folder):
        for img in temporal_images_folder:
            remove(path.abspath(f'{TEMPORAL_IMAGE_FOLDER}/{img}'))
    
def get_font(font=None):
    if font == 'funny':
        ttf_font ='SeymourOne-Regular.ttf'
    else:
        ttf_font = 'bungeespice.ttf'
    
    font_location = f'{settings.BASE_DIR}/static/cats/fonts/{ttf_font}'
    return ImageFont.truetype(font_location, DEFAULT_FONT_SIZE)

def get_locations(image_selected):

    _, filename = str(image_selected).split('/')
    name, _  = filename.split('.')
    uuid = randint(1, 9999)

    print(name)
    new_name = f'{name}{uuid}.webp'
    new_location = f'{TEMPORAL_IMAGE_FOLDER}/{new_name}'
    current_location = f'{settings.MEDIA_ROOT}/{image_selected}'

    return (current_location, new_location, new_name)

def get_centred_position(size_tuple):
    image_width, image_height = size_tuple
    x = (image_width) // 2
    y = (image_height) // 2
    return (x, y)


def put_text_on_image(image_selected, text, font=None):
    cheack_temporal_folder()

    location, new_location, new_name = get_locations(image_selected)
        
    img = Image.open(location)
    selected_font = get_font(font)
    draw = ImageDraw.Draw(img)
    
    draw.text((get_centred_position(img.size)), text, anchor="mm" ,fill=(255,255,255), font=selected_font)

    img.save(new_location)
    return new_name
    
