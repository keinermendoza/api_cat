from random import randint
from django.conf import settings
from PIL import Image, ImageFont, ImageDraw

def put_text_on_image(image_selected, text=None, selected_font=None):
    
    name, _ = str(image_selected).split('.')
    uuid = randint(1, 9999)

    image_location = f'{settings.MEDIA_ROOT}/{image_selected}'
    
    img = Image.open(image_location)

    draw = ImageDraw.Draw(img)
    if selected_font is None:
        selected_font = 'RethinkSans-ExtraBold.ttf'

    font_location = f'{settings.BASE_DIR}/assets/fonts/{selected_font}'

    font = ImageFont.truetype(font_location, 24)
    # font = ImageFont.load_default()

    if text is None:
        text = 'Hola Mundo'
    
     # Obtener el tamaño de la imagen
    image_width, image_height = img.size

    # Obtener el tamaño del texto
    # text_width, text_height = draw.textsize(text, font)

    # Calcular la posición para centrar el texto
    x = (image_width) // 2
    y = (image_height) // 2

    draw.text((x, y), text, anchor="mm" ,fill=(255,255,255), font=font)


    location = img.save(f'{settings.MEDIA_ROOT}/temporal/{name}{uuid}.webp')
    return location
    
 