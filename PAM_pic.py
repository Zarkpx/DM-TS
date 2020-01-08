import numpy as np
import pandas as pd
import random
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('test_pic.jpg')

def dis(v1,v2):
    dist = ((v1[0]-v2[0])**2+(v1[1]-v2[1])**2+(v1[2]-v2[2])**2)**0.5
    return dist

#计算总距离，以此来判断是否更新中心点
def all_dis(vv1,v2):
    dist_all = 0.0
    for i in range(len(vv1)):
        dist_all = dist_all + dis(v2,img[vv1[i][0]][vv1[i][1]])       
    return dist_all
        



k1_5 = []
#随机抽取5个点
for x in range(5):
    i = random.randint(0,len(img))
    j = random.randint(0,len(img[0]))
    k1_5.append(img[i][j].tolist())
#print(k1_5)
class1 = []
class2 = []
class3 = []
class4 = []
class5 = []
class1_dist = 0.0
class2_dist = 0.0
class3_dist = 0.0
class4_dist = 0.0
class5_dist = 0.0
for m in range(10):
    #随机生成5个新中心点
    k1_5_new = []
    for x in range(5):
        i = random.randint(0,len(img)-1)
        j = random.randint(0,len(img[0])-1)
        k1_5_new.append(img[i][j].tolist())
    #如果新中心点总距离小于旧中心点总距离 则更新
    if len(class1)!=0 and len(class2)!=0 and len(class3)!=0 and len(class4)!=0 and len(class5)!=0:
        print(k1_5_new)
        if all_dis(class1,k1_5_new[0]) < class1_dist:
            k1_5[0] = k1_5_new[0]
        if all_dis(class2,k1_5_new[1]) < class2_dist:
            k1_5[1] = k1_5_new[1]
        if all_dis(class3,k1_5_new[2]) < class3_dist:
            k1_5[2] = k1_5_new[2]
        if all_dis(class4,k1_5_new[3]) < class4_dist:
            k1_5[3] = k1_5_new[3]
        if all_dis(class5,k1_5_new[4]) < class5_dist:
            k1_5[4] = k1_5_new[4]
    #新一轮迭代，清空上次结果
    class1 = []
    class2 = []
    class3 = []
    class4 = []
    class5 = []
    class1.append(k1_5[0])
    class2.append(k1_5[1])
    class3.append(k1_5[2])
    class4.append(k1_5[3])
    class5.append(k1_5[4])
    #判断各像素与中心点的距离
    for i in range(len(img)):
        for j in range(len(img[0])):
            dis_list = []
            for m in range(5):
                dis_list.append(dis(img[i][j],k1_5[m]))
                idx = dis_list.index(min(dis_list))
                if idx == 0:
                    class1.append([i,j])
                    class1_dist += dis_list[idx]
                elif idx == 1:
                    class2.append([i,j])
                    class2_dist += dis_list[idx]
                elif idx == 2:
                    class3.append([i,j])
                    class3_dist += dis_list[idx]
                elif idx == 3:
                    class4.append([i,j])
                    class4_dist += dis_list[idx]
                elif idx == 4:
                    class5.append([i,j])
                    class5_dist += dis_list[idx]
                    
print(len(class1))
plt.imshow(img)
f1 = plt.figure(4)
#plt.subplot(211)
plt.scatter([x[0] for x in class1],[x[1] for x in class1],marker = 'x',color = 'm',label='1')
plt.scatter([x[0] for x in class2],[x[1] for x in class2],marker = 'o',color = 'r',label='2')
plt.scatter([x[0] for x in class3],[x[1] for x in class3],marker = '+',color = 'g',label='3')
plt.scatter([x[0] for x in class4],[x[1] for x in class4],marker = 's',color = 'b',label='4')
plt.scatter([x[0] for x in class5],[x[1] for x in class5],marker = 'D',color = 'y',label='5')
