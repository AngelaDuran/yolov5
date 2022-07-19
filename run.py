#Run this file to get packages working
import torch
import utils
display = utils.notebook_init()  # checks
print(display)

#Use this in terminal to run
#python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images

#python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/labImages