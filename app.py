from cgitb import text
import tkinter as tk
from tkinter import Button, Canvas, filedialog, Text
import os
from turtle import color, title
from pdf2image import convert_from_path
import cv2
import numpy as np
from PIL import Image
from datetime import datetime
from time import localtime
from PIL import Image, ImageFont, ImageDraw


def openFile() :
    filepath = filedialog.askopenfilename()
    popplerpath = r".\source\Release-22.04.0-0\poppler-22.04.0\Library\bin"
    pdfpath = (r"" + filepath)
    print(pdfpath)
    #########################################
    from pdf2image import convert_from_path
    import cv2
    import numpy as np
    from PIL import Image
    import os

    pages = convert_from_path(pdf_path=pdfpath, poppler_path=popplerpath)
    for page in pages:
        page.save("temp/image.jpg", "JPEG")

    img = cv2.imread("temp/image.jpg")
    resize = cv2.resize(img, (1240,1755), interpolation = cv2.INTER_AREA)
    cv2.imwrite("temp/image.jpg",resize)
    #########################################
    img = cv2.imread("temp/image.jpg") # read the image with the QR code
    rows, cols, _ = img.shape #to get cordinations
    print("Rows", rows) #show Y
    print("Cols", cols) #show X
    cut_image = img[1525: 1690, 215:380] #cut the QR code
    cv2.imwrite("temp/cut.jpg",cut_image) #save the croped QR code
    img1 = Image.open("temp/cut.jpg") #open the QR code
    img2 = Image.open("source/v1.jpg") #open the template (Face1)
    area = (500, 500, 665, 665) #the cordinates area to put the QR code
    img2.paste(img1, area) #paste the QR code on the template
    title_font = ImageFont.truetype('source/Myriad Pro Bold.ttf', 25) #date font and size
    current_date_time = datetime.now() #get local datetime
    if current_date_time.day < 10: #to add 0 before the day when the values is less than 10
        day = ("0" + str(current_date_time.day))
    else:
        day = str(current_date_time.day) #convert day into string      
    month = str(current_date_time.month) #convert month into string
    year = str(current_date_time.year) #convert year into string
    title_text = (day + "-" + month + "-" + year) #add dashs to seperate the date values
    image_editable = ImageDraw.Draw(img2) #convert image into editable object
    image_editable.text((585,453), title_text, (0, 0, 0), font=title_font) #write the date on the image
    # img2.show()
    # img2.save("temp/face1.pdf") #save image as pdfd
    img2.save('temp/face1.pdf', 'PDF', resolution=300.0) #save image as pdfd
    os.system(r".\temp\face1.pdf") #to open pdf automatically after saving it
    #########################################
    img = cv2.imread("temp/image.jpg") # take the original image
    original = cv2.imread("source/v2.jpg") # take the template (Face 2)
    rows, cols, _ = img.shape #to get cordinations
    print("Y", rows) #show Y
    print("X", cols) #show X
    cut_image_1 = img[547:772, 85:1157] #cut the first portion
    cut_image_2 = img[950:1279, 85:1157] #cut the second portion
    resized_image_1 = cv2.resize(cut_image_1, (880,179), interpolation = cv2.INTER_AREA) #resize the first portion of the image
    # cv2.imshow("cut-image_1", resized_image_1) #show the resized first portion of the image
    cv2.imwrite("temp/ri1.jpg",resized_image_1) #save the first portion
    resized_image_2 = cv2.resize(cut_image_2, (880,186), interpolation = cv2.INTER_AREA) #resize the second portion of the image
    # cv2.imshow("cut-image_2", resized_image_2) #show the resized second portion of the image
    cv2.imwrite("temp/ri2.jpg",resized_image_2) #save the second portion
    c_img_1 = Image.open("temp/ri1.jpg") #open the resized first portion
    c_img_2 = Image.open("temp/ri2.jpg") #open the resized first portion
    o_img = Image.open("source/v2.jpg") #open the template (Face2)
    area_1 = (438, 309, 1318, 488) #the cordinates area to put the first portion
    area_2 = (438, 523, 1318, 709) #the cordinates area to put the second portion
    o_img.paste(c_img_1, area_1) #paste the first portion on the template
    o_img.paste(c_img_2, area_2) #paste the second portion on the template
    # o_img.show()
    # o_img.save("temp/face2.pdf") #save image as pdfd
    o_img.save('temp/face2.pdf', 'PDF', resolution=300.0) #save image as pdfd
    os.system(r".\temp\face2.pdf") #to open pdf automatically after saving it
    
    # os.remove('temp/face1.pdf')
    # os.remove('temp/face2.pdf')
    os.remove('temp/cut.jpg')
    os.remove('temp/ri1.jpg')
    os.remove('temp/ri2.jpg')
    os.remove('temp/image.jpg')



windows = tk.Tk()
canvas = tk.Canvas(windows, height=400, width=400, bg="#fffcf2")
button = Button(text="Convert",command=openFile,height=3, width=12,bg="#A7FFE4", activeforeground="#FF1E1E")
button.pack()
canvas.pack()
windows.title("Vignette 1.0 By ADIL ALAMI")
windows.iconbitmap("source/Aeidle.ico")

windows.mainloop()

###################################

