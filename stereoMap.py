import numpy as np
import sys
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

### FOV Method
def depthFOV(leftCamPos, rightCamPos, camHeight, focalLength, sensor_h, sensor_v):
  # positions in meters
  # sensor dimensions and focal length in mm

  # Regular focal length
  h_FOV = np.arctan(sensor_h/(2*focalLength))
  v_FOV = np.arctan(sensor_v/(2*focalLength))

  l = rightCamPos-leftCamPos # Camera separation
  
  leftImg = cv2.imread('/content/left.jpg', 0)
  rightImg = cv2.imread('/content/right.jpg', 0)
  
  leftImg.shape
  midLine_h = leftImg.shape[1]/2
  midLine_v = leftImg.shape[0]/2

  for i in range(len(data.get("Object"))):
    objectLx = data.get("Lx")[i]
    objectRx = data.get("Rx")[i]

    pre_alpha = np.arctan((objectLx-midLine_h)*h_FOV/midLine)
    pre_beta = np.arctan((midLine_h-objectRx)*h_FOV/midLine)

    alpha = np.pi/2-pre_alpha
    beta = np.pi/2-pre_beta

    print(data.get("Object")[i] + ": ")
    #print("\tAlpha: " + str(np.degrees(alpha)))
    #print("\tBeta: " + str(np.degrees(beta)))

    # z = depth
    z = l*((np.sin(alpha)*(np.sin(beta)))/np.sin(alpha+beta))
    print("\tz: " + str(z))

    objectLy = data.get("Ly")[i]
    objectRy = data.get("Ry")[i]

    x = leftCamPos+(z/np.tan(alpha))
    #x2 = rightCamPos-(d/np.tan(beta)) # confirmation with other angle

    angleVL = np.arctan((midLine_v-objectLy)*v_FOV/midLine_v)
    angleVR = np.arctan((midLine_v-objectRy)*v_FOV/midLine_v)

    y = camHeight+(z*np.tan(angleVL))

    print("\tX: " + str(x))
    #print("\tX2: " + str(x2))

    print("\ty: " + str(y))
    print("")
