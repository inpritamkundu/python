# import required classes

from PIL import Image, ImageDraw, ImageFont
import os

path = os.path.join(os.getcwd(), 'src', 'textOnImage')

# create Image object with the input image

image = Image.open(
    r''+path+'\image\certificate.jpg')

# initialise the drawing context with
# the image object as background

draw = ImageDraw.Draw(image)

# desired size

fontName = ImageFont.truetype(
    r''+path+'\style\DancingScript.ttf', 150)

fontCourse = ImageFont.truetype(
    r''+path+'\style\Asul-Regular.ttf', 95)

fontDate = ImageFont.truetype(
    r''+path+'\style\Asul-Regular.ttf', 75)

fontCertificateNum = ImageFont.truetype(
    r''+path+'\style\Asul-Regular.ttf', 50)


# starting position of the certificate number

(x, y) = (2500, 100)
certificateNum = "C.No. :- 123456dwhdkgs"
nameColor = 'rgb(0, 0, 0)'  # black color

# draw the message on the background
w, h = draw.textsize(certificateNum, font=fontCertificateNum)

draw.text((x-(w/2), y), certificateNum,
          fill=nameColor, font=fontCertificateNum)


# starting position of the name

(x, y) = (1727, 1100)
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
w, h = draw.textsize(courseName, font=fontCourse)

draw.text((x-(w/2), y), courseName, fill=courseColor, font=fontCourse)


# starting position of the date

(x, y) = (1050, 2120)
courseName = "2/04/2020"
courseColor = 'rgb(0, 0, 0)'  # black color

# draw the message on the background
w, h = draw.textsize(courseName, font=fontDate)

draw.text((x-(w/2), y), courseName, fill=courseColor, font=fontDate)

# save the edited image

image.save(r''+path+'\image\\'+userName+'.pdf')
