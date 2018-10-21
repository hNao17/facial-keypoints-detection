import cv2 as cv
import pandas as pd
import numpy as np
import os


'''Train / Test Data Import******************************************************************************************'''
data_dir = "data"
train_dir = "train"
train_csv = "training.csv"
test_dir = "test"
test_csv = "test.csv"

df_train = pd.read_csv(os.path.join(data_dir, train_csv))
df_test = pd.read_csv(os.path.join(data_dir, test_csv))

'''******************************************************************************************************************'''


'''# of Train / Test Images******************************************************************************************'''

n_train = df_train['Image'].size
n_test = df_test['Image'].size

print("# of training images: {}".format(n_train))
print("# of test images: {}".format(n_test))

'''******************************************************************************************************************'''


'''Save Train & Test Images to External Folder***********************************************************************'''


def save_images(img_arr, img_type, img_dir):

    for i, img in enumerate(img_arr):
        img = np.fromstring(img, dtype=int, sep=' ')
        img = np.reshape(img, newshape=(96, 96))

        fn = img_type + str(i) + ".png"

        cv.imwrite(os.path.join(data_dir, img_dir, fn), img)

        print("Saving {} to {}".format(fn, os.path.join(data_dir, img_dir)))


train_arr = df_train['Image'].tolist()
test_arr = df_test['Image'].tolist()

save_images(train_arr, img_type="train", img_dir=train_dir)
save_images(test_arr, img_type="test", img_dir=test_dir)

'''******************************************************************************************************************'''


'''Find Image Indices with 15 Keypoints******************************************************************************'''


df_kp = df_train.iloc[:, 0:30]
counter = 0
idxs = []

id_dict = {}
kp_dict = {}

for i in range(n_train):

    if True in df_train.iloc[i, 0:30].isna().values:
        continue
    else:
        counter += 1
        idxs.append(i)

        # image
        img = df_train.iloc[i, 30]
        img = np.fromstring(img, dtype=float, sep=' ')
        img = np.reshape(img, newshape=(96, 96))/ 255
        id_dict[i] = img

        # keypoints
        kp = df_kp.iloc[i].values.tolist()
        kp_dict[i] = kp

print("# of Images with 15 keypoints = {}".format(counter))

'''******************************************************************************************************************'''

