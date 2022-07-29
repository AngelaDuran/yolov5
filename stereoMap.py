import numpy as np
import sys
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

### FOV Method
def depthFOV(data, leftCamPos, rightCamPos, camHeight, focalLength, sensor_h, sensor_v):
  ''' Example Parameters for Testing:
        leftCamPos = 0.26 m
        rightCamPos = 0.56 m
        camHeight = 0.175 m
        focalLength = 4.26 mm
        sensor_h = 6.17 mm
        sensor_v = 4.55 mm
  '''
  # positions in meters
  # sensor dimensions and focal length in mm

  # Regular focal length
  h_FOV = np.arctan(sensor_h/(2*focalLength))
  v_FOV = np.arctan(sensor_v/(2*focalLength))

  l = rightCamPos-leftCamPos # Camera separation
  
  #leftImg = cv2.imread('/content/left.jpg', 0)
  #rightImg = cv2.imread('/content/right.jpg', 0)

  #Angela Modifications
  leftImg = cv2.imread('./data/labImages/left1.jpg', 0)
  rightImg = cv2.imread('./data/labImages/right1.jpg', 0)
  
  leftImg.shape
  midLine_h = leftImg.shape[1]/2
  midLine_v = leftImg.shape[0]/2

  for i in range(len(data.get("Object"))):
    objectLx = data.get("Lx")[i]
    objectRx = data.get("Rx")[i]

    pre_alpha = np.arctan((objectLx-midLine_h)*h_FOV/midLine_h)
    pre_beta = np.arctan((midLine_h-objectRx)*h_FOV/midLine_h)

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
    #x2 = rightCamPos-(z/np.tan(beta)) # confirmation with other angle

    angleVL = np.arctan((midLine_v-objectLy)*v_FOV/midLine_v)
    angleVR = np.arctan((midLine_v-objectRy)*v_FOV/midLine_v)

    y = camHeight+(z*np.tan(angleVL))

    print("\tX: " + str(x))
    #print("\tX2: " + str(x2))

    print("\ty: " + str(y))
    print("")

    

### Ruler Method
def depthRuler(data, leftCamPos, rightCamPos, camHeight, h_rulerDist, v_rulerDist, pixelsToCm_h, pixelsToCm_v):
  ''' Example Parameters for Testing:
        leftCamPos = 0.26 m
        rightCamPos = 0.56 m
        camHeight = 0.175 m
        h_rulerDist = 0.40 m
        v_rulerDist = 0   <- unused, doesn't matter
        pixelsToCm_h = 75  
        pixelsToCm_v = 0  <- unused, doesn't matter
  '''
  
  # positions and distances in meters
  
  # "Magic" conversion numbers
  magicNum_h = pixelsToCm_h*100*h_rulerDist
  magicNum_v = pixelsToCm_v*100*v_rulerDist

  l = rightCamPos-leftCamPos # Camera separation
  
  leftImg = cv2.imread('/content/left.jpg', 0)
  rightImg = cv2.imread('/content/right.jpg', 0)
  
  leftImg.shape
  midLine_h = leftImg.shape[1]/2

  for i in range(len(data.get("Object"))):
    objectLx = data.get("Lx")[i]
    objectRx = data.get("Rx")[i]

    alpha = np.pi/2-np.arctan((objectLx-midLine_h)/magicNum_h)
    beta = np.pi/2-np.arctan((midLine_h-objectRx)/magicNum_h)

    print(data.get("Object")[i] + ": ")
    #print("\tAlpha: " + str(np.degrees(alpha)))
    #print("\tBeta: " + str(np.degrees(beta)))

    z = l*((np.sin(alpha)*(np.sin(beta)))/np.sin(alpha+beta))

    print("\tz: " + str(z))

    objectLy = data.get("Ly")[i]
    objectRy = data.get("Ry")[i]

    x = leftCamPos+(z/np.tan(alpha))
    #x2 = rightCamPos-(z/np.tan(beta))

    print("\tX: " + str(x))
    #print("\tX2: " + str(x2))
    print("")
