import tensorflow as tf
import numpy as np
import cv2
import detect_face
import matplotlib.pyplot as plt
import math
from scipy import misc
 
img = misc.imread('001.jpg')
 
sess = tf.Session()
pnet, rnet, onet = detect_face.create_mtcnn(sess, None)
 
# pnet, rnet, onet are 3 funtions
 
minsize = 20
threshold = [0.6, 0.7, 0.7]
factor = 0.709
df_result, df_points_result = detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
 
# df_points_result is faceNumber X 10
# need transpose to 10 X faceNumber
df_points_result = np.transpose(df_points_result)
 
vec_vec_points = []
for subPoints in df_points_result:
    # subPoints: [x1,x2,x3,x4,x5,y1,y2,y3,y4,y5]
    # image axis, so convert nose to (48,48)
    # Points of small faces are too close to compute correct Homography Matrix.
    # So, scale points.
    deltaX = 48-subPoints[2]
    deltaY = 48-subPoints[7]
    vec_vec_points.append([[subPoints[0]+deltaX, subPoints[5]+deltaY],
                           [subPoints[1]+deltaX, subPoints[6]+deltaY],
                           [subPoints[2]+deltaX, subPoints[7]+deltaY],
                           [subPoints[3]+deltaX, subPoints[8]+deltaY],
                           [subPoints[4]+deltaX, subPoints[9]+deltaY]])
 
 
n_face = df_result.shape[0]
print('detected face number: {}'.format(n_face))
print(df_result)
 
plt.figure('faces')
i = 0
plt_nrow = n_face / 5
plt_nrow = plt_nrow + int(n_face != plt_nrow * 5)
plt_ncol = 5
crop_face = []
crop_face_adjust = []
size_img = (96,96)
pts_dst = np.array([[29.0,24.0],[67.0,24.0],[48.0,48.0],[28.0,62.0],[68.0,62.0]]) # measure
for subfaceRec in df_result:
    i = i + 1
    subfaceRec = subfaceRec.astype(int)
    img_a_face = img[subfaceRec[1]:subfaceRec[3], subfaceRec[0]:subfaceRec[2]]
    crop_face.append(img_a_face)
 
    # adjust image
    pts_src = np.array(vec_vec_points[i-1])
    H, _ = cv2.findHomography(pts_src, pts_dst)
    img_a_face_adjust = cv2.warpPerspective(img_a_face, H, (img_a_face.shape[1]+30, img_a_face.shape[0]+30))
    crop_face_adjust.append(img_a_face_adjust)
 
    # resize image
    img_a_face = cv2.resize(img_a_face, size_img, interpolation=cv2.INTER_CUBIC)
 
    # display and show
    print('plt_nrow:{}, plt_ncol:{}, i:{}'.format(plt_nrow, plt_ncol, i))
    plt.subplot(plt_nrow, plt_ncol, i)
    plt.imshow(img_a_face)
 
    cv2.rectangle(img, (subfaceRec[0], subfaceRec[1]), (subfaceRec[2], subfaceRec[3]), (0, 255, 0), 2)
 
 
# show face adjust
i = 0
plt.figure('faces_adjust')
for sub_img_ad in crop_face_adjust:
    timg = cv2.resize(sub_img_ad, size_img, interpolation=cv2.INTER_CUBIC)
    i = i+1
    plt.subplot(plt_nrow, plt_ncol, i)
    plt.imshow(timg)
 
# draw points
plt.figure('img')
for subPoints in df_points_result:
    # subPoints: [x1,x2,x3,x4,x5,y1,y2,y3,y4,y5]
    cv2.circle(img, (subPoints[0], subPoints[5]), 2, (255, 0, 0), -1) # Red left eye
    cv2.circle(img, (subPoints[1], subPoints[6]), 2, (0, 0, 255), -1) # Blue right eye
    cv2.circle(img, (subPoints[2], subPoints[7]), 2, (0, 255, 0), -1) # Green nose
    cv2.circle(img, (subPoints[3], subPoints[8]), 2, (255, 255, 0), -1) # yellow left mouse
    cv2.circle(img, (subPoints[4], subPoints[9]), 2, (0, 255, 255), -1) # cyan right mouse
 
plt.imshow(img)
plt.show()
 
sess.close()