import additionals.inference as infer
import additionals.globals as gv
import argparse
import threading
import socket
import keyboard

frame = None
inference = None

client = None

def tracking():
    global frame
    global inference
    global chat_id
    while gv.DETECTION_RUNNING:
        boxes, scores, classes = inference.next()
        if gv.PERSON_DETECTED:
            update.message.reply_text("Pertsona dago")

thread1 = threading.Thread(target=tracking)

def piztu():
    global thread1
    gv.DETECTION_RUNNING = True
    thread1.start()

def itzali():
    global frame
    global thread1
    thread1.stop()
    gv.DETECTION_RUNNING = False
    frame = None
    
def main(model_path, ip, port):
    global inference

    inference = infer(model_path)

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((ip,port))

    while True:
        boxes, scores, classes = inference.next()
        for i in classes:
            if classes[i] in gv.DETECTIONS:
                if boxes[i][0] < gv.X_L_MAX and boxes[i][1] < gv.X_L_MAX and boxes[i][1] < gv.X_L_MAX and boxes[i][1] < gv.X_L_MAX:
                    conn.send('1')
                elif boxes[i][0] < gv.X_L_MAX and boxes[i][1] < gv.X_L_MAX and boxes[i][1] < gv.X_L_MAX and boxes[i][1] < gv.X_L_MAX:
                    conn.send('2')
                elif boxes[i][0] < gv.X_L_MAX and boxes[i][1] < gv.X_L_MAX and boxes[i][1] < gv.X_L_MAX and boxes[i][1] < gv.X_L_MAX:
                    conn.send('3')
        if keyboard.read_key() == "q" or keyboard.read_key() == "Q":
            break
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
    parser.add_argument('--model_path', value='models/yolov7-tiny-nms.trt', metavar='path', required=True,
                        help='the path to model')
    parser.add_argument('--ip', value='192.168.1.28', required=True,
                        help='ip of ESP path to model')
    parser.add_argument('--port', value='8800', required=True,
                        help='the path to model')
    args = parser.parse_args()

    main()
