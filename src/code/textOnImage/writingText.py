# import required classes

from PIL import Image, ImageDraw, ImageFont
import os

path = os.path.join(os.getcwd(), 'src', 'code', 'textOnImage')

# create Image object with the input image

image = Image.open(
    r''+path+'\image\certificate.jpg')

# initialise the drawing context with
# the image object as background

draw = ImageDraw.Draw(image)

# desired size

fontName = ImageFont.truetype(
    r''+path+'\style\Roboto-Black.ttf', 100)

# starting position of the name

(x, y) = (1727, 1200)
userName = "Puja Kumari Gupta"
nameColor = 'rgb(0, 0, 0)'  # black color

# draw the message on the background
w, h = draw.textsize(userName, font=fontName)

draw.text((x-(w/2), y), userName, fill=nameColor, font=fontName)


# starting position of the course name

(x, y) = (1727, 1550)
courseName = "Angular"
courseColor = 'rgb(0, 0, 0)'  # black color

# draw the message on the background
w, h = draw.textsize(courseName, font=fontName)

draw.text((x-(w/2), y), courseName, fill=courseColor, font=fontName)


# starting position of the date

(x, y) = (1050, 2120)
courseName = "2/04/2020"
courseColor = 'rgb(0, 0, 0)'  # black color

# draw the message on the background
w, h = draw.textsize(courseName, font=fontName)

draw.text((x-(w/2), y), courseName, fill=courseColor, font=fontName)

# save the edited image

image.save(r''+path+'\image\greet.pdf')
