import argparse
import socket
import jetson.inference
import jetson.utils
import additionals.globals as gv

import urllib.request
import http

base = "http://192.168.1.137/"


def transfer(my_url):   #use to send and receive data
    try:
        n = urllib.request.urlopen(base + my_url).read()
        n = n.decode("utf-8")
        return n

    except http.client.HTTPException as e:
        return e

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")      # '/dev/video0' for V4L2 and 'csi://0' for csi
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file
render_img = False

def main():

    while True:
        img = camera.Capture()
        detections = net.Detect(img)
        if render_img:
            display.Render(img)
            display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
        for detection in detections:
            class_id = detection.ClassID
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
                    check = transfer("1")
                    if check != "1":
                        print("An error ocurred while transfer")
                # Si esta en la parte izquierda-central de la imagen
                elif gv.X_L_MIN < x1 < gv.X_L_MAX and  gv.X_M_MIN < x2 < gv.X_M_MAX:
                    check = transfer('2')
                    if check != "2":
                        print("An error ocurred while transfer")
                # Si esta en la parte central de la imagen
                elif gv.X_M_MIN < x1 < gv.X_M_MAX and  gv.X_M_MIN < x2 < gv.X_M_MAX:
                    check = transfer('3')
                    if check != "3":
                        print("An error ocurred while transfer")
                # Si esta en la parte central-derecha de la imagen
                elif gv.X_M_MIN < x1 < gv.X_M_MAX and  gv.X_R_MIN < x2 < gv.X_R_MAX:
                    check = transfer('4')
                    if check != "4":
                        print("An error ocurred while transfer")
                # Si esta en la parte derecha de la imagen
                elif gv.X_R_MIN < x1 < gv.X_R_MAX and  gv.X_R_MIN < x2 < gv.X_R_MAX:
                    check = transfer('5')
                    if check != "5":
                        print("An error ocurred while transfer")
                # Si esta de izquierda a derecha ocupando casi toda la imagen
                elif gv.X_L_MIN < x1 < gv.X_L_MAX/2 and  gv.X_R_MIN < x2 < (gv.X_R_MAX - (gv.X_R_MAX-gv.X_R_MIN)/2):
                    check = transfer('6')
                    if check != "6":
                        print("An error ocurred while transfer")
    
if __name__ == '__main__':
    main()
