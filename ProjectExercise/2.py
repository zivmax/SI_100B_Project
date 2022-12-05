import matplotlib.pyplot as mp
import cv2

# 1、读取图像，并把图像转换为灰度图像并显示
img = cv2.imread(r"C:\Users\fer20\Desktop\project1\SI_100B_Project\ProjectExercise\UserData\plate21.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换了灰度化
img2 = img_gray.T
cv2.imshow('gra_y', img2)  # 显示图片
cv2.waitKey(0)

# 2、将灰度图像二值化，设定阈值是100
img_thre = img_gray
cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY, img_thre)
img3 = img_thre.T
cv2.imshow('threshold', img3)
cv2.waitKey(0)

# 4、分割字符
def image_split_column(a)->list:
    a = a.T
    ret = []
    startList = []
    endList = []
    height = a.shape[0]
    width = a.shape[1]
    white_max = 0
    black_max = 0
    # 计算每一列的黑白色像素总和
    for i in range(width):
        s = 0  # 这一列白色总数
        t = 0  # 这一列黑色总数
        for j in range(height):
            if a[j][i] == 255:
                s += 1
            if a[j][i] == 0:
                t += 1
        white_max = max(white_max, s)
        black_max = max(black_max, t)
        startList.append(s)
        endList.append(t)


    n = 1
    while n < width - 2:
        n += 1
        if endList[n] > 0.01 * black_max:
            start = n
            for m in range(start + 1, width - 1):
                if startList[m] > 0.99 * white_max:  # 0.95这个参数请多调整，对应下面的0.05
                    end = m
                    break
                else:
                    end = start+1
            n = end
            if end - start > 10:
                cut = a[:, start - 30:end + 30]
                ret.append(cut.T)
                cv2.imshow('caijian', cut.T)
                cv2.waitKey(0)

    return ret


c = image_split_column(img_thre)
print(c)
