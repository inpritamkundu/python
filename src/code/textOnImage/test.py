import os
from PIL import Image, ImageDraw, ImageFont

new = os.path.join(os.getcwd(), 'src', 'code', 'textOnImage')
image = Image.open(
    r''+new+'\image\certificate.jpg')
image.show()
print(new)
