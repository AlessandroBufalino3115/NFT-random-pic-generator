
from PIL import Image, ImageDraw, ImageFilter
from random import randrange
import time
import os

if __name__ == '__main__':

    start = time.time()

    file_list=os.listdir(r"C:\Users\alexh\PycharmProjects\NFT\layers") #the name of all the folders

    folder_contents = []
    inside_inside_folder = []

    for x in file_list:
        folder_contents.append("C:\\Users\\alexh\\PycharmProjects\\NFT\\layers\\" + x)   # this saves the names of all the directories

    for x in range(len(folder_contents)):
        inside_fodler = os.listdir(r"" + folder_contents[x]) # this gives me all the components inside the actual fodler

        for y in range(len(inside_fodler)):
            inside_fodler[y] = folder_contents[x] + "\\"+  inside_fodler[y]

        inside_inside_folder.append(inside_fodler)






    for x in range(10):

        im1 = Image.open(inside_inside_folder[0][randrange(len(inside_inside_folder[0]))])
        im7 = Image.open(inside_inside_folder[1][randrange(len(inside_inside_folder[1]))])
        im3 = Image.open(inside_inside_folder[2][randrange(len(inside_inside_folder[2]))])
        im2 = Image.open(inside_inside_folder[3][randrange(len(inside_inside_folder[3]))])
        im4 = Image.open(inside_inside_folder[4][randrange(len(inside_inside_folder[5]))])
        im6 = Image.open(inside_inside_folder[5][randrange(len(inside_inside_folder[6]))])
        im8 = Image.open(inside_inside_folder[6][randrange(len(inside_inside_folder[7]))])

        images = [im1,im2,im3,im4,im6,im7,im8]  # this is size layer

        back_img = im1.copy()

        for y in range(1,7): # this si imaages size
            back_img.paste(images[y],(0, 0),images[y])

        back_img.save('images/is_this_new_' + str(x) +'.png' , quality=95)

        print(str(x)+" done")

    end = time.time()

    print("done, time elapsed: " + str(end - start))
    pass
