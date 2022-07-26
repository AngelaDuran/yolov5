import numpy as np
import sys
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

def depthFOV(leftCamPos, rightCamPos, ):
  ### FOV Method
  # Less accurate (for some reason)

  h_FOV = np.arctan(36/(2*26))
  v_FOV = np.arctan(24/(2*26))

  l = rightCamPos-leftCamPos # Camera separation

  pixelsToCm = 75 
  referenceRulerDist = 40
  magicNum = pixelsToCm*referenceRulerDist; # "Magic" conversion number

  leftImg.shape
  midLine = leftImg.shape[1]/2
  midLine_v = leftImg.shape[0]/2

  for i in range(len(data.get("Object"))):
    objectLx = data.get("Lx")[i]
    objectRx = data.get("Rx")[i]

    pre_alpha = np.arctan((objectLx-midLine)*h_FOV/midLine)
    pre_beta = np.arctan((midLine-objectRx)*h_FOV/midLine)

    alpha = np.pi/2-pre_alpha
    beta = np.pi/2-pre_beta

    print(data.get("Object")[i] + ": ")
    #print("\tAlpha: " + str(np.degrees(alpha)))
    #print("\tBeta: " + str(np.degrees(beta)))

    d = l*((np.sin(alpha)*(np.sin(beta)))/np.sin(alpha+beta))

    # z = depth
    print("\tz: " + str(d))

    objectLy = data.get("Ly")[i]
    objectRy = data.get("Ry")[i]

    x = leftCamPos+(d/np.tan(alpha))
    #x2 = rightCamPos-(d/np.tan(beta)) # confirmation with other angle


  angleVL = np.arctan((midLine_v-objectLy)*v_FOV/midLine_v)
  angleVR = np.arctan((midLine_v-objectRy)*v_FOV/midLine_v)
  
  # Future code in progress for depth calculation using vertical image shift
  # dd = l*((np.sin(np.pi/2-angleHL)*(np.sin(np.pi/2-angleHR)))/np.sin(np.pi/2-angleHL+np.pi/2-angleHR))
  # print(str(angleHL) +" "+str(angleHR))
  # print(str(dd))

  # -674/angle = midline_v/v_FOV
  # angle = -674*v_FOV/midline_v

  y = 17.5+(d*np.tan(angleVL))

  print("\tX: " + str(x))
  #print("\tX2: " + str(x2))

  print("\ty: " + str(y))
  print("")



  print("")
