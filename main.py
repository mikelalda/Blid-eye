import additionals.inference as infer
import additionals.globals as gv
import argparse
import socket
import keyboard
    
def main(model_path, ip, port):
    global inference

    inference = infer(model_path)

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((ip,port))

    while True:
        boxes, scores, classes = inference.next()
        for i in classes:
            if classes[i] in gv.DETECTIONS:
                '''
                Suponiendo que boxes[0] is x.min, boxes[1] is y.min, boxes[2] is width and boxes[3] is height
                '''
                # Si esta en la parte izquierda de la imagen
                if gv.X_L_MIN < boxes[i][0] < gv.X_L_MAX and  gv.X_L_MIN < boxes[i][0] + boxes[i][2] < gv.X_L_MAX:
                    conn.send('1')
                # Si esta en la parte izquierda-central de la imagen
                elif gv.X_L_MIN < boxes[i][0] < gv.X_L_MAX and  gv.X_M_MIN < boxes[i][0] + boxes[i][2] < gv.X_M_MAX:
                    conn.send('2')
                # Si esta en la parte central de la imagen
                elif gv.X_M_MIN < boxes[i][0] < gv.X_M_MAX and  gv.X_M_MIN < boxes[i][0] + boxes[i][2] < gv.X_M_MAX:
                    conn.send('3')
                # Si esta en la parte central-derecha de la imagen
                elif gv.X_M_MIN < boxes[i][0] < gv.X_M_MAX and  gv.X_R_MIN < boxes[i][0] + boxes[i][2] < gv.X_R_MAX:
                    conn.send('4')
                # Si esta en la parte derecha de la imagen
                elif gv.X_R_MIN < boxes[i][0] < gv.X_R_MAX and  gv.X_R_MIN < boxes[i][0] + boxes[i][2] < gv.X_R_MAX:
                    conn.send('5')
                # Si esta de izquierda a derecha ocupando casi toda la imagen
                elif gv.X_L_MIN < boxes[i][0] < gv.X_L_MAX/2 and  gv.X_R_MIN < boxes[i][0] + boxes[i][2] < (gv.X_R_MAX - (gv.X_R_MAX-gv.X_R_MIN)/2):
                    conn.send('6')
        if keyboard.read_key() == "q" or keyboard.read_key() == "Q":
            break
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create an alarm')
    parser.add_argument('--model_path', value='models/yolov7-tiny-nms.trt', metavar='path', required=True,
                        help='the path to model')
    parser.add_argument('--ip', value='192.168.1.28', required=True,
                        help='ip of ESP path to model')
    parser.add_argument('--port', value='8800', required=True,
                        help='the path to model')
    args = parser.parse_args()

    main()
