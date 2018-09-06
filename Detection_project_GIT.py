
# coding: utf-8

# In[ ]:


import sys
import dlib
import numpy as np
import hdf5storage as h5f
from skimage import io
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X=h5f.loadmat("X.mat")["X"]
y_om=h5f.loadmat("y_om.mat")["y"].T
y_smile=h5f.loadmat("y_smile.mat")["y"].T

def get_landmarks(file_name):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    img = io.imread(file_name)
    detections = detector(img,1)
    win = dlib.image_window()
    win.set_image(img)
    for k, d in enumerate(detections):
        shape = predictor(img, d)
        win.add_overlay(d)
        win.add_overlay(shape)
        X_test = np.empty([68, 2], dtype = int)
        for b in range(68):
            X_test[b][0] = shape.part(b).x
            X_test[b][1] = shape.part(b).y
    return X_test,win
def SVC_om(X,y_om,X_test):
    clf_om = SVC(kernel='linear', probability=True, tol=1e-3);
    clf_om.fit(X, y_om.ravel())
    vec_om=clf_om.predict_proba(X_test)
    y_model_om=clf_om.predict(X_test)
    print('Open mouth detection:')
    print("neutral : " + str(accuracy_score([0],y_model_om)) + " (" + str(np.round(np.array(vec_om[0][0])*100)) + " %)")
    print("open mouth : " + str(accuracy_score([1],y_model_om))+ " (" + str(np.round(np.array(vec_om[0][1])*100)) + " %)")
def SVC_smile(X,y_smile,X_test):
    clf_smile = SVC(kernel='linear', probability=True, tol=1e-3);
    clf_smile.fit(X, y_smile.ravel())
    vec_smile=clf_smile.predict_proba(X_test)
    y_model_smile=clf_smile.predict(X_test)
    print('Smile detection:')
    print("neutral : " + str(accuracy_score([0],y_model_smile)) + " (" + str(np.round(np.array(vec_smile[0][0])*100)) + " %)")
    print("smile : " + str(accuracy_score([1],y_model_smile))+ " (" + str(np.round(np.array(vec_smile[0][1])*100)) + " %)")        

cmdLineArg = len(sys.argv)
i=0
for argv in sys.argv:
    if (cmdLineArg>1 and cmdLineArg<=len(sys.argv)):
        i=i+1
        print( "Detection image  " + str(sys.argv[i]))
        X_test, win = get_landmarks(str(sys.argv[i]))
        X_test = np.reshape(X_test,(1,136))                           
        SVC_om(X,y_om,X_test);
        SVC_smile(X,y_smile,X_test);

