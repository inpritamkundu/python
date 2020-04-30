# import required classes

from PIL import Image, ImageDraw, ImageFont
import os
import string


def generateCerti(userName, courseName, courseDays, courseDate):

    # capitalizing the arguments
    userName = string.capwords(userName)
    courseName = string.capwords(courseName)
    courseDays = string.capwords(courseDays)

    # adding cno to certificate number
    # certificateNum = 'C.No :- '+certificateNum

    path = os.path.join(os.getcwd(), 'src', 'teckat', 'api', 'functions')

    # create Image object with the input image

    image = Image.open(
        r''+path+'\generatedCertificate\originalCertificate.jpg')

    # initialise the drawing context with
    # the image object as background

    draw = ImageDraw.Draw(image)

    # desired size

    fontName = ImageFont.truetype(
        r''+path+'\style\DancingScript.ttf', 130)

    fontCourse = ImageFont.truetype(
        r''+path+'\style\Asul-Regular.ttf', 75)

    fontDays = ImageFont.truetype(
        r''+path+'\style\Asul-Regular.ttf', 65)
    fontDate = ImageFont.truetype(
        r''+path+'\style\Asul-Regular.ttf', 70)

    # fontCertificateNum = ImageFont.truetype(
    #     r''+path+'\style\Asul-Regular.ttf', 50)

    # starting position of the certificate number

    # (x, y) = (2500, 100)
    # nameColor = 'rgb(0, 0, 0)'  # black color

    # # draw the message on the background
    # w, h = draw.textsize(certificateNum, font=fontCertificateNum)

    # draw.text((x-(w/2), y), certificateNum,
    #           fill=nameColor, font=fontCertificateNum)

    # starting position of the name

    (x, y) = (1800, 990)
    nameColor = 'rgb(54, 127, 193)'  # black color

    # draw the message on the background
    w, h = draw.textsize(userName, font=fontName)

    draw.text((x-(w/2), y), userName, fill=nameColor, font=fontName)

    # starting position of the course name

    (x, y) = (1775, 1370)
    courseColor = 'rgb(0, 0, 0)'  # black color

    # draw the message on the background
    w, h = draw.textsize(courseName, font=fontCourse)

    draw.text((x-(w/2), y), courseName, fill=courseColor, font=fontCourse)

    # # starting position of the No. of Days

    (x, y) = (1595, 1582)
    courseColor = 'rgb(0, 0, 0)'  # black color

    # draw the message on the background
    w, h = draw.textsize(courseDays, font=fontDays)

    draw.text((x-(w/2), y), courseDays, fill=courseColor, font=fontDays)

    # starting position of the date

    (x, y) = (1800, 1850)
    courseColor = 'rgb(0, 0, 0)'  # black color

    # draw the message on the background
    w, h = draw.textsize(courseDate, font=fontDate)

    draw.text((x-(w/2), y), courseDate, fill=courseColor, font=fontDate)

    # save the edited image

    pdfPath = path+'\generatedCertificate\\'+userName+'.jpg'

    image.save(r''+pdfPath)

    # return "%s" % pdfPath


# generateCerti("123456dwhdkgs", "Puja Kumari Gupta",
#               "Angular", "2/04/2020", "abc")

generateCerti("siba shankar mahapatra", "Budding Entrepreneurs : India is waiting for startups to innovate ",
              "1 Day", "30/04/2020")
