import numpy as np
from sklearn import neighbors
from PIL import Image
import os
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.externals import joblib
import test

import cv2

if __name__ == "__main__":
    data = []
    labels = []
    img_dir ='./after_labels/traindata'
    img_name = os.listdir(img_dir)
    img_dir2 = './after_labels/traindata_'
    img_name2 = os.listdir(img_dir2)
    for i in range(len(img_name)):
        path2 = os.path.join(img_dir2, img_name2[i])
        image = cv2.imread(path2)
        im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = im.reshape(-1)
        data.append(image)

        y_temp = img_name[i][0]
        labels.append(y_temp)
    
    y = LabelBinarizer().fit_transform(labels)

    x = np.array(data)
    y = np.array(labels)

    # 分割训练集与测试集
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size= 0.2)

    # 训练模型并保存
    clf = neighbors.KNeighborsClassifier()
    clf.fit(x_train,y_train)
    joblib.dump(clf, './knn.pkl')

    # 展示模型的结果
    pre_y_train = clf.predict(x_train)
    pre_y_test = clf.predict(x_test)
    classname = ['1','2','3','b','c','n','v','x','z']
    print(classification_report(y_train,pre_y_train,target_names= classname))
    print(classification_report(y_test,pre_y_test,target_names= classname))


