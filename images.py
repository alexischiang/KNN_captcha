from PIL import Image,ImageEnhance
import cv2
import os
import numpy as np



def check_vertical(img, threashold, outDir, index):
    '''
    :param img:
    :param threashold: 阀值
    :param outDir: 保存位置
    :return:
    '''
    w, h = img.size
    pixdata = img.load()
 
    x_array = []
    startX = 0
    endX = 0
    for x in range(w):
        b_count = 0
        for y in range(h):
            if pixdata[x, y] <= threashold:
                b_count += 1
        if b_count > 0:
            if startX == 0:
               startX = x
        elif b_count == 0:
            if startX != 0:
               endX = x
               x_array.append({'startX':startX, 'endX':endX})
               startX = 0
               endX = 0
    if len(x_array) == 4:
        img.save('./success-images/'+str(index)+'.png')
        print(str(index) + ' :ok!')
        for i, item in enumerate(x_array):
            box = (item['startX'], 0, item['endX'], h)
            img.crop(box).save(outDir + str(index) + '-' +str(i+1) + ".png")
    else:
        print(str(index) + ' :no!')


def import_cutting(index):
    img = Image.open('./images/'+ str(index) + '.png')
    check_vertical(img,100,'./after/',index)


    

# # 逐个打开图片
# img_dir = './images'
# img_name = os.listdir(img_dir)
# for i in range(len(img_name)):
#     path = os.path.join(img_dir,img_name[i])