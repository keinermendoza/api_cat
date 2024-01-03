from random import randint
from os import path, listdir, remove
from django.conf import settings
from PIL import Image, ImageFont, ImageDraw

DEFAULT_FONT_SIZE = 32
LIMIT_TEMPORAL_IMAGES = 20
TEMPORAL_IMAGE_FOLDER = f'{settings.MEDIA_ROOT}/temporal'

def cheack_temporal_folder():
    temporal_images_folder = listdir(TEMPORAL_IMAGE_FOLDER)

    if LIMIT_TEMPORAL_IMAGES < len(temporal_images_folder):
        for img in temporal_images_folder:
            remove(path.abspath(f'{TEMPORAL_IMAGE_FOLDER}/{img}'))
    
def get_font(font=None):
    if font is None:
        font = 'RethinkSans-ExtraBold.ttf'
    font_location = f'{settings.BASE_DIR}/assets/fonts/{font}'
    return ImageFont.truetype(font_location, DEFAULT_FONT_SIZE)

def get_locations(image_selected):

    name, _ = str(image_selected).split('/')
    uuid = randint(1, 9999)

    new_location = f'{TEMPORAL_IMAGE_FOLDER}/{name}{uuid}.webp'
    current_location = f'{settings.MEDIA_ROOT}/{image_selected}'

    return (current_location, new_location)

def get_centred_position(size_tuple):
    image_width, image_height = size_tuple
    x = (image_width) // 2
    y = (image_height) // 2
    return (x, y)


def put_text_on_image(image_selected, text, selected_font=None):
    cheack_temporal_folder()

    name, new_name = get_locations(image_selected)
        
    img = Image.open(name)
    font = get_font(selected_font)
    draw = ImageDraw.Draw(img)
    
    draw.text((get_centred_position(img.size)), text, anchor="mm" ,fill=(255,255,255), font=font)

    img.save(new_name)
    return new_name
    
