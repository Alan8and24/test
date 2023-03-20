#对题目进行分析，发现需要进行文件夹之间的处理，因此需引入os，还有随机性要引入random，计算灰度值需要用到cv2以及numpy
#此文件要达到分配图片的目的，需要与marvel和data文件放在同一路径下
#分配的本质即为复制，后按一定比例随机分别放入两个文件夹中。随机————使用random打乱，分配复制文件————shutil模块
#最后在train中随机抽一张照片计算其灰度值与灰度值差，要计算灰度值则需要用到numpy库


import os
import random
import shutil
import cv2
import numpy as np


# 遍历marvel文件夹中的子文件夹
for folder in os.listdir("marvel"):
    if os.path.isdir(os.path.join("marvel", folder)):
        # 创建train和test子文件夹
        os.makedirs(os.path.join("data/train", folder), exist_ok=True)
        os.makedirs(os.path.join("data/test", folder), exist_ok=True)

        # 获取该子文件夹下的所有图片文件路径
        img_paths = [os.path.join("marvel", folder, filename) for filename in os.listdir(os.path.join("marvel", folder)) if filename.endswith((".jpg", ".png", ".jpeg"))]

        # 打乱图片文件路径的顺序
        random.shuffle(img_paths)

        # 计算分割点
        split_index = int(0.7 * len(img_paths))

        # 将图片复制到train和test子文件夹中
        for i, img_path in enumerate(img_paths):
            if i < split_index:
                shutil.copy(img_path, os.path.join("data/train", folder))
            else:
                shutil.copy(img_path, os.path.join("data/test", folder))

# 从train文件夹中随机选择一张图片
folder = random.choice(os.listdir("data/train"))
img_path = os.path.join("data/train", folder, random.choice(os.listdir(os.path.join("data/train", folder))))

# 读取图片并转为灰度图像
img = cv2.imread(img_path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#计算灰度值
mean_gray = np.mean(gray_img)

print(f"这张照片的灰度值为: {mean_gray}")

# 计算灰度图像的方差
variance = np.var(gray_img)

print(f"这张照片灰度值的方差为: {variance}")
