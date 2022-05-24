import cv2

img = cv2.imread("img/sushe.jpg")
# 加载级联分类器
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 获取灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 检测图像中所有的人脸
# def detectMultiScale(self, image, scaleFactor=None, minNeighbors=None, flags=None, minSize=None, maxSize=None):
# image：待检测的图像，通常为灰度图像
# scaleFactor：表示在前后两次相继的扫描中，搜索窗口的缩放比例
# minNeighbors：表示构成检测目标的相邻矩形的最小个数。默认值为3，表示有3个以上的检测标记存在时，才认为人脸的存在。如果希望提高检测的准确率，可以将该值设置的更大，但同时可能会让一些人脸无法被检测到
# flags：不常用参数，一般省略。
# minSize：目标的最小尺寸，小于这个尺寸的目标将被忽略
# maxSize：目标的最大尺寸，大于这个尺寸的目标将被忽略
# 该函数的返回值是目标对象的矩形框向量组。

# 通过detectMultiScale函数返回的是人脸的矩形框向量组，
# 包括左上角坐标(x,y)，长宽(w,h)。
# 而绘制人脸圆形框只需要将矩形的中心设置为圆心，矩形的宽度一般设置为半径即可。
faces = faceCascade.detectMultiScale(gray)
print(faces)
print("该图一共有{0}个人脸".format(len(faces)))
for (x, y, w, h) in faces:
    # 绘制人脸圆形框,将矩形的中心设置为圆心，矩形的宽度一般设置为半径。
    cv2.circle(img, (int((2 * x + w) / 2), int((2 * y + h) / 2)), int(w / 2), (0, 255, 0), 2)
cv2.imshow("result", img)
cv2.waitKey()
cv2.destroyAllWindows()
