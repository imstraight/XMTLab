import cv2
import numpy as np
import os

#以下代码段用于测试编号为ID的摄像头
ID = 0
while(1):
    cap = cv2.VideoCapture(ID, cv2.CAP_DSHOW)
    ret, frame = cap.read()
    if ret == False:
        print("error")
    else:
        print(ID)
        while(1):
            width = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
            height = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            print(width, height)
            ret, frame = cap.read()
            cv2.resize(frame, (int(width), int(height)), interpolation=cv2.INTER_CUBIC)
            cv2.imshow("l", frame)
            print('yes')
            key = cv2.waitKey(10)
        break


VideoId_Left = 0
VideoId_Right = 1

#选择摄像头

videoLeftUp = cv2.VideoCapture(VideoId_Left, cv2.CAP_DSHOW)
videoRightUp = cv2.VideoCapture(VideoId_Right, cv2.CAP_DSHOW)

width = (int(videoLeftUp.get(cv2.CAP_PROP_FRAME_WIDTH)))
height = (int(videoLeftUp.get(cv2.CAP_PROP_FRAME_HEIGHT)))
num = 1



#以下代码段用于查找摄像头编号
# ID = 1
# while(1):
#     cap = cv2.VideoCapture(ID, cv2.CAP_DSHOW)
#     # cap2 = cv2.VideoCapture(VideoId_Right, cv2.CAP_DSHOW)
#     # get a frame
#     ret, frame = cap.read()
#     if ret == False:
#         ID += 1
#         print(ID)
#     else:
#         print(ID)
#         while(1):
#             width = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
#             height = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#             print(width, height)
#             ret, frame = cap.read()
#             cv2.resize(frame, (int(width), int(height)), interpolation=cv2.INTER_CUBIC)
#             cv2.imshow("l", frame)
#
#             # width = (int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH)))
#             # height = (int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#             # print(width, height)
#             # ret2, frame2 = cap2.read()
#             # if cap2 == False:
#             #     print("null")
#             # cv2.resize(frame2, (int(width), int(height)), interpolation=cv2.INTER_CUBIC)
#             # cv2.imshow("r", frame2)
#             print('111')
#             key = cv2.waitKey(10)
#         break

#以下代码段用于测试保存照片
# while (videoLeftUp.isOpened()):
#     retLeftUp, frameLeftUp = videoLeftUp.read()
#     retRightUp, frameRightUp = videoRightUp.read()
#
#     frameLeftUp = cv2.resize(frameLeftUp, (int(width), int(height)), interpolation=cv2.INTER_CUBIC)
#     frameRightUp = cv2.resize(frameRightUp, (int(width), int(height)), interpolation=cv2.INTER_CUBIC)
#
#     frameUp = np.hstack((frameLeftUp, frameRightUp))
#     cv2.imwrite('C:/Users/xyy_X/Desktop/image/' + str(num) + '.jpg', frameUp)
#     #frameLeftUp.save('C:/Users/xyy_X/Desktop/image/' + str(num) + '.jpg')
#     cv2.imshow('frame', frameUp)
#     print('111')
#     key = cv2.waitKey(10)
#     if int(key) == 113:
#         break

videoLeftUp.release()
videoRightUp.release()
