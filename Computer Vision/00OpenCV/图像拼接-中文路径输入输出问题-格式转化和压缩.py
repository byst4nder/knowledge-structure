# coding=utf-8
import os
import cv2
import numpy as np


def cv_image_fo_chinese(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    # imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
    return cv_img


def coIMG(imagefile):
    image = cv_image_fo_chinese(imagefile)
    # print(image.shape)
    img1 = image[106:1106, 170:1570]
    img2 = image[106:1106, 1813:3213]
    img3 = image[1190:2190, 165:1565]

    img_fill = np.zeros((1000, 1400, 3), np.uint8)
    border_v = np.zeros((1000, 30, 3), np.uint8)
    stack_h_1 = np.hstack((img1, border_v, img2))
    stack_h_2 = np.hstack((img3, border_v, img_fill))
    border_h = np.zeros((30, 1400*2 + 30, 3), np.uint8)
    stack_v = np.vstack((stack_h_1, border_h, stack_h_2))
    return stack_v


num = 0
root = "../data/"
output = "../output/"
if not os.path.exists(output):
    os.mkdir(output)
for folder in os.listdir(root):
    outfolder = os.path.join(output, folder)
    if not os.path.exists(outfolder):
        os.mkdir(outfolder)
    for file in os.listdir(os.path.join(root, folder)):
        file_path = os.path.join(root, folder, file)
        resImg = coIMG(file_path)
        outImg_path = os.path.join(outfolder, file)
        cv2.imencode(".jpg", resImg, [int(cv2.IMWRITE_JPEG_QUALITY), 95])[1].tofile(outImg_path)
        # cv2.imencode(".jpg", resImg)[1].tofile(outImg_path)
        # 上下两个差别：一个185Mb，一个185MB,所以，上面是下面的默认情况。
        num += 1

print(num)
