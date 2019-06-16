import numpy as np
from sklearn import neighbors
from PIL import Image
import os
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.externals import joblib
import cv2

def resize_pic(path):
    image = Image.open(path)
    image = image.resize((11,17))
    image.save('./test/'+'resized.png')

def reshape_pic():
    data = []
    img = cv2.imread('./test/'+'resized.png')
    im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = im.reshape(-1)
    data.append(img)
    return np.array(data)

def knn_predict(path,data):
    clf = joblib.load(path)
    pre = clf.predict(data)
    classname = ['1','2','3','b','c','n','v','x','z']
    print(pre)

if __name__ == "__main__":
    resize_pic('./after_labels/testdata/106-3.png')
    data = reshape_pic()
    print(data)
    path = './knn.pkl'
    knn_predict(path,data)