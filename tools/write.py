# coding:utf-8
import os
from PIL import Image
from PIL import ImageFile

def changeSize(dir, writedir):
    f = open(writedir,'a')
    files = os.listdir(dir)
    for file in files:
        path = os.path.join(dir, file)
        if os.path.isdir(path):
            changeSize(path, writedir)
        
        else:
            back =  os.path.splitext(file)[1]
            if back==".jpg" or back==".png" or back==".pgm" or back==".bmp":
                img = Image.open(path)
                (x, y) = img.size
                # out = img.resize((34, 40), Image.ANTIALIAS)
                # out = out.convert('L')
                # out.save(path)
                f.write(path + ' 1 0 0 ' + str(x) + ' ' + str(y) + '\n')
    f.close()

if __name__=="__main__":
    path = r"C:\Users\huoxi\Desktop\pics\second\palm_test_4"
    writepath = r"C:\Users\huoxi\Desktop\pics\second\palm_test_4\at.txt"
    changeSize(path, writepath)