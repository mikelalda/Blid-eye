# Jetson Nano Object detection alarm

Procedure to make inference in Jetson Nano with yolo-v7. [Here](Object_detection_methods.md) you could find more information about object detection methods

## Set up Jetson Nano

Go to [this](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#intro) step by step tutorial.

## Install dependecies and download packages

Firs of all we will have to install python dependecies. For that open a terminal an execute the followin commands.

```bash
sudo apt-get update
sudo apt-get install python3-pip -y
sudo apt-get install dialog -y # Download the model
sudo apt-get install v4l2loopback-dkms # To display the image
sudo modprobe v4l2loopback
sudo apt-get install nano 
```

## Preàre the docker container

First of all we need to clone the repository of jetson inference and go to the folder jetson_inference.

```bash
git clone https://github.com/mikelalda/Blind-eye.git

```

Clone jetson-inference repository

```bash
git clone https://github.com/dusty-nv/jetson-inference.git


```

Each time to run the container follow the next steps:

```bash
cd jetdon-inference
docker/run.sh --volume path_to/Blind-eye/:/Blind-eye
```

## Run inference

In the file Alarm-Yolo/main.py we need to change the line 10 with ESP8266 IP address.

![](assets/20230412_121807_image.png)

Once having done all the steps, run this in the docker terminal.

```bash
cd /Blind-eye
python3 main.py
```
