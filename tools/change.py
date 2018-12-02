# coding:utf-8
import os
from PIL import Image
from PIL import ImageFile
def change(x, y, max):
    if x > y:
        x_s = max
        y_s = x_s * y / x
    else:
        y_s = max
        x_s = y_s * x / y
    return (x_s, y_s)

def changeSize(dir):
    files = os.listdir(dir)
    for file in files:
        path = os.path.join(dir, file)
        if os.path.isdir(path):
            changeSize(path)
        
        else:
            back =  os.path.splitext(file)[1]
            if back==".jpg" or back==".png" or back==".pgm" or back==".JPG":
                img = Image.open(path)
                (x, y) = img.size
                out = img.resize((30, 30), Image.ANTIALIAS)
                # out = out.convert('L')
                out.save(path)

def changeGray(dir):
    files = os.listdir(dir)
    for file in files:
        path = os.path.join(dir, file)
        if os.path.isdir(path):
            changeGray(path)
        
        else:
            back =  os.path.splitext(file)[1]
            if back==".jpg" or back==".png" or back==".pgm":
                img = Image.open(path)
                out = img.convert('L')
                out.save(path)

if __name__ == "__main__":
    ImageFile.LOAD_TRUNCATED_IMAGES = True  
    path_2 = r"F:\Lab\haar\pos_30"
    # path_3 = r"F:\Lab\haar\pos_test_1"
    # path_4 = r"F:\Lab\haar\pos_test_2"
    # path_3 = r"H:\third\thumb_6"
    changeSize(path_2)
    # changeSize(path_3)
    # changeSize(path_4)
    # changeGray(path_2)