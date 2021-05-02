import os
import cv2
import pickle
import numpy as np
from imutils import paths
from sklearn.preprocessing import LabelBinarizer
import tensorflow as tf
from tensorflow import keras
from keras.models import Model
from keras.models import load_model
import matplotlib.pyplot as plt


def predict(img_path):
    model = load_model('test_model_128_5_32_2.model')
    lbl_bin = pickle.loads(open('supporting_file.pickle',"rb").read())
    X=[]
    lsize=128
    X.append(cv2.resize(cv2.imread(img_path),(lsize,lsize)))
    X=np.array(X,dtype="float")/255.0
    preds = model.predict(X)
    key=preds.argmax(axis=1)[0]
    lbl=lbl_bin.classes_[key]
    return lbl, preds[0][key]*100


    # ax.set_title("{}: {:.2f}%".format(lbl,preds[i][key]*100))

# label, perсent = predict(r"C:\Users\Nat\flowers\1.jpg")
# print(label, perсent)