import argparse
import socket
import jetson.inference
import jetson.utils
import additionals.globals as gv

import urllib.request
import http

server_ip = "192.168.1.137/"
server_port = 80
soc = socket.socket()
soc.connect((server_ip, server_port))
def transfer(mydata):   #use to send and receive data
    soc.sendall(mydata)

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")      # '/dev/video0' for V4L2 and 'csi://0' for csi
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file
render_img = False

names = ['unlabeled', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 
         'traffic light', 'fire hydrant', 'street sign', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 
         'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'hat', 'backpack', 'umbrella', 
         'shoe', 'eye' 'glasses', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports' 'ball', 'kite', 
         'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'plate', 'wine glass', 
         'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 
         'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'mirror', 'dining table', 'window', 'desk', 'toilet', 
         'door', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 
         'blender', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

def main():

    while True:
        img = camera.Capture()
        detections = net.Detect(img)
        if render_img:
            display.Render(img)
            display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
        for detection in detections:
            print(names[detection.ClassID])
            class_id = names[detection.ClassID-1]
            x1 = detection.Left   
            y1 = detection.Top    
            x2 = detection.Right  
            y2 = detection.Bottom 
            if class_id in gv.DETECTIONS:
                '''
                Suponiendo que boxes[0] is x.min, boxes[1] is y.min, boxes[2] is width and boxes[3] is height
                '''
                # Si esta en la parte izquierda de la imagen
                if gv.X_L_MIN < x1 < gv.X_L_MAX and  gv.X_L_MIN < x2 < gv.X_L_MAX:
                    print(1)
                    check = transfer("1")
                    if check != "1":
                        print("An error ocurred while transfer")
                # Si esta en la parte izquierda-central de la imagen
                elif gv.X_L_MIN < x1 < gv.X_L_MAX and  gv.X_M_MIN < x2 < gv.X_M_MAX:
                    print(2)
                    check = transfer('2')
                    if check != "2":
                        print("An error ocurred while transfer")
                # Si esta en la parte central de la imagen
                elif gv.X_M_MIN < x1 < gv.X_M_MAX and  gv.X_M_MIN < x2 < gv.X_M_MAX:
                    print(3)
                    check = transfer('3')
                    if check != "3":
                        print("An error ocurred while transfer")
                # Si esta en la parte central-derecha de la imagen
                elif gv.X_M_MIN < x1 < gv.X_M_MAX and  gv.X_R_MIN < x2 < gv.X_R_MAX:
                    print(4)
                    check = transfer('4')
                    if check != "4":
                        print("An error ocurred while transfer")
                # Si esta en la parte derecha de la imagen
                elif gv.X_R_MIN < x1 < gv.X_R_MAX and  gv.X_R_MIN < x2 < gv.X_R_MAX:
                    print(5)
                    check = transfer('5')
                    if check != "5":
                        print("An error ocurred while transfer")
                # Si esta de izquierda a derecha ocupando casi toda la imagen
                elif gv.X_L_MIN < x1 < gv.X_L_MAX/2 and  gv.X_R_MIN < x2 < (gv.X_R_MAX - (gv.X_R_MAX-gv.X_R_MIN)/2):
                    print(6)
                    check = transfer('6')
                    if check != "6":
                        print("An error ocurred while transfer")
    
if __name__ == '__main__':
    main()
