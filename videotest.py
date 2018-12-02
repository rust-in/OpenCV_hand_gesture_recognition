#-*- coding:utf-8 -*- 
import cv2
import numpy as np

def find_face(img): #检测并标识人脸及眼睛
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #对图像进行灰度化

    face_cascade = cv2.CascadeClassifier(r'D:\Anaconda3\envs\opencv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml') #调用人脸识别模型，默认安装
    eye_cascade = cv2.CascadeClassifier(r'D:\Anaconda3\envs\opencv\Lib\site-packages\cv2\data\haarcascade_eye.xml') #调用眼睛识别模型，默认安装
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #对识别后的人脸进行画图处理
    for (x, y, w, h) in faces:
        # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) #画方块
        cv2.circle(img,(int((x+x+w)/2),int((y+y+h)/2)),int(w/2),(255,0,0),2) #画圆
        roi_gray = gray[y:y+h, x:x+w] #只识别出现在脸的范围内的眼睛相似物
        roi_color = img[y:y+h, x:x+w] 
        eyes = eye_cascade.detectMultiScale(roi_gray) #同理
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    
    return img

def find_fist(img): #和thumb手势太相似
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    fist_cascade = cv2.CascadeClassifier(r'\xml\fist_data_v1\cascade.xml') 
    
    fists = fist_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in fists:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) 

    
    return img

def find_palm(img): #检测并标识手掌手势
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    fist_cascade = cv2.CascadeClassifier(r'xml\palm.xml')
    fists = fist_cascade.detectMultiScale(gray, 1.05, 5) #exp 1.1 5/7 
    
    return fists

def draw_palm(list, img):
    for (x, y, w, h) in list:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) #画方块
    return img

def find_thumb(img): #检测并标识大拇指手势
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fist_cascade = cv2.CascadeClassifier(r"xml\thumb.xml")
    fists = fist_cascade.detectMultiScale(gray, 1.1, 15, flags=cv2.CASCADE_SCALE_IMAGE)  #v20_20 1.1 30 #v6 v17_20 
    
    return fists

def draw_thumb(list, img):
    for (x, y, w, h) in list:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2) #画方块
    return img

if __name__ == "__main__":
    cap = cv2.VideoCapture(0) #调用摄像头，参数0为默认摄像头

    # count = 1
    while(1):
        # get a frame
        ret, img = cap.read()     

        # if cv2.waitKey(1) & 0xFF == ord('p'): #按p拍照
        #     cv2.imwrite(str(count) + '.jpg', img)
        #     count += 1   

        p_list = find_palm(img)
        t_list = find_thumb(img)
        fin = draw_thumb(t_list, draw_palm(p_list, img))

        cv2.imshow("capture", fin)

        if cv2.waitKey(1) & 0xFF == ord('q'): #按q退出
            break

    cap.release()
    cv2.destroyAllWindows() 