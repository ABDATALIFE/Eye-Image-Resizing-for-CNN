#%%
import os
import cv2
import numpy as np


#%%
root_path = 'C:/Users/Abdul Basit Aftab/Desktop/Images'
    




#%%
#cropping and loading dataset
def data_load(root_path, scale=(224,224)):
  categories =  os.listdir(root_path)
  x = []
  y =[]
  for i, cat in enumerate(categories):
    img_path = root_path
    images = os.listdir(img_path)
    for image in images:
        img = cv2.imread(os.path.join(img_path, image), 1)
        height, width,channel = img.shape
        if width == 2144:
            img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
            img = img[0:450,100:550]
            img = cv2.resize(img,(224,224))
            #return img
        elif width == 1424:
            img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
            img = img[100:550,0:450]
            img = cv2.resize(img,(224,224))
            #return img
        elif width == 2048:
            img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
            img = img[0:450,80:530]
            img = cv2.resize(img,(224,224))
            #return img
        elif width == 1536:
            img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
            img = img[80:530,0:450]
            img = cv2.resize(img,(224,224))
            #return img
        elif width == 4288:
            img = cv2.resize(img, (0,0), fx=0.1, fy=0.1)
            img = img[0:280,20:380]
            img = cv2.resize(img,(224,224))
            #return img
        elif width == 2848:
            img = cv2.resize(img, (0,0), fx=0.1, fy=0.1)
            img = img[20:380,0:280]
            img = cv2.resize(img,(224,224))
            #return img

        x.append(img)
        y.append(i)
  return np.array(x), np.array(y)

#%%


Xtrain,ytrain = data_load(root_path)


#%%

for i,images in enumerate(Xtrain):
    name = "image_save.jpg"
    full_name = str(i)+name
    cv2.imwrite(full_name,images)
    



