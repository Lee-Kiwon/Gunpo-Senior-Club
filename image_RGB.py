import sys, os
sys.path.append(os.pardir)
import matplotlib.pyplot as plt
# from simple_convnet import SimpleConvNet
from matplotlib.image import imread

img = imread('23.png')

print(img.shape)

plt.imshow(img)
plt.axis('off')
plt.show()



red=img
# red[:, :, 1]=0
# red[:, :, 2]=0
#
# plt.imshow(img)
# plt.axis('off')
# plt.show()



# red 지우고 해보기
# green=img
# green[:, :, 0]=0
# green[:, :, 2]=0
#
# plt.imshow(img)
# plt.axis('off')
# plt.show()



# red, green 지우고 해보기
blue=img
blue[:, :, 0]=0
blue[:, :, 1]=0

plt.imshow(img)
plt.axis('off')
plt.show()
