"""
LBPH方法的基本原理
LBPH（Local Binary Patterns Histogram，局部二值模式直方图）所使用的模型基于LBP(局部二值模式)算法。LBP最早是被作为一种有效的纹理描述算子提出的，由于在表述图像局部纹理特征上效果明显，而得到广泛应用。
LBP算法的基本原理是，将像素点A的值与其最邻近的8个像素点的值逐一比较：
如果A的像素值大于其临近点的像素值，则得到0
如果A的像素值小于其临近点的像素值，则得到1
最后，将像素点A与其周围8个像素点比较所得到的0、1值连接起来，得到一个8位的二进制序列，将该二进制序列转换为十进制数作为点A的LBP值。
LBPH实现步骤
在OpenCV中，它提供函数cv2.face.LBPHFaceRecognizer_create()生成LBPH识别器实例模型，然后应用cv2.face_FaceRecognizer.train()函数完成训练，最后用cv2.face_FaceRecognizer.predict()函数完成人脸识别。



cv2.face.LBPHFaceRecognizer_create()生成LBPH识别器实例模型
def LBPHFaceRecognizer_create(radius=None, neighbors=None, grid_x=None, grid_y=None, threshold=None):

radius：半径值，默认1
neighbors：领域点的个数，默认采用8领域，根据需要可以计算更多的领域点
grid_x：将LBP特征图像划分为一个个单元格时，每个单元格在水平方向上的像素个数。默认值8，即将LBP特征图像在行方向上以8个像素为单位分组
grid_y：将LBP特征图像划分为一个个单元格时，每个单元格在垂直方向上的像素个数。默认值8，即将LBP特征图像在列方向上以8个像素为单位分组
threshold：预测时所使用的阈值。如果大于该阈值，就认为没有识别到任何目标对象


cv2.face_FaceRecognizer.train()函数完成训练
cv2.face_FaceRecognizer.train(self, src, labels)

src：训练图像，相当于前面识别图像的训练集，用来学习的人脸图像
labels：标签，人脸图像所对应的标签


cv2.face_FaceRecognizer.predict()函数完成人脸识别
cv2.face_FaceRecognizer.predict(self, src)

src：需要识别的人脸图像
返回值有两个，一个返回前面训练集匹配的人脸识别的标签label，另一个是用来衡量识别结果与原有模型之间的距离。通常情况下，小于50的值是可以接受的，如果该值大于80则认为差别较大。
"""

import cv2
import numpy as np

images = []
images.append(cv2.imread("img/taotao1.jpg", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("img/taotao2.jpg", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("img/zhurui1.jpg", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("img/zhurui2.jpg", cv2.IMREAD_GRAYSCALE))
labels = [0, 0, 1, 1]
# 生成LBPH识别器实例模型
recognizer = cv2.face.LBPHFaceRecognizer_create()
# 训练图像
recognizer.train(images, np.array(labels))
predict_image = cv2.imread('img/taotao3.jpg', cv2.IMREAD_GRAYSCALE)
label, confidence = recognizer.predict(predict_image)

print(label)
if label==0:
    print("匹配的人脸为涛涛")
elif label==1:
    print("匹配的人脸为瑞瑞")
print("confidence=", confidence)

"""
从输出结果来看，标签值为“0”，置信区间为42.13175573481297，这说明3图被识别为涛涛对应的人脸图像。不过，数据量越大越准确
"""