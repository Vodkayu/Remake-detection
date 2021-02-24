import cv2
from PIL import Image
import scipy.io as scio
from numpy import *
import time
import os
import numpy as np
from skimage.feature import local_binary_pattern



def Tran(src, drc,datarc):

    img = cv2.imread(src , 0)

    cv2.destroyAllWindows()
    tic = time.time()
    radius = 1
    n_points = radius * 8
    res = local_binary_pattern(img, n_points, radius)
    #toc = time.time()
    cv2.imwrite(drc, res)  # 保存lbp图像
    #tic = time.time()
    gg = splitimage(drc, 5,5)
    j=0
    for i in gg[0]:
        j=j+i
    #toc = time.time()
    scio.savemat(datarc, {'train_feature': gg[0]})  # 保存



# 分块切割并提取出其lbp特征向量，切割不懂的看fenge.py的注释
def splitimage(src, rownum, colnum):
    img = Image.open(src)
    # print(type(img.size))
    w = img.width
    h =img.height
    # w, h = img.size
    if rownum <= h and colnum <= w:

        print('开始处理图片切割, 请稍候...')

        s = os.path.split(src)

        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]


        num = 0
        rowheight = int(h/colnum)

        ggg = []

        for r in range(rownum):
            for c in range(colnum):

                box = (c *rowheight , r * rowheight, c *rowheight + rowheight, r * rowheight + rowheight)
                box = np.array(img.crop(box))

                hist1 = np.histogram(box, bins=256)
                hist = hist1[0] / (box.size)

                ggg.append(hist)

                num = num + 1

        #print('图片切割完毕，共生成 %s 张小图片。' % num)

    else:
        print('不合法的行列切割参数！')
    #print(np.array(ggg))
    return np.array(ggg).reshape(1, -1)
