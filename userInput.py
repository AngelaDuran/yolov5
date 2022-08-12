#Author: Angela Duran
#want user to specify camera information here
'''
leftCamPos = 0.26 
rightCamPos = 0.56 
camHeight = 0.175 
focalLength = 4.26 
sensor_h = 6.17 
sensor_v = 4.55 
'''

def stereoParam():

    leftCamPos = float(input("Enter Left Camera Position in m: "))
    rightCamPos = float(input("Enter Right Camera Position in m: "))
    camHeight = float(input("Enter Camera Height in m: "))
    focalLength = float(input("Enter Focal Length in mm: "))
    sensor_h = float(input("Enter horizontal sensor length in mm: "))
    sensor_v = float(input("Enter vertical sensor length in mm: "))

    return [leftCamPos, rightCamPos, camHeight, focalLength, sensor_h, sensor_v]



''' Example Parameters for Testing:
        leftCamPos = 0.26 m
        rightCamPos = 0.56 m
        camHeight = 0.175 m
        h_rulerDist = 0.40 m
        v_rulerDist = 0   <- unused, doesn't matter
        pixelsToCm_h = 75  
        pixelsToCm_v = 0  <- unused, doesn't matter
'''
def rulerParam():
    leftCamPos = float(input("Enter Left Camera Position in m: "))
    rightCamPos = float(input("Enter Right Camera Position in m: "))
    camHeight = float(input("Enter Camera Height in m: "))
    horzRulerLength = float(input("Enter Horizontal Ruler Length in m: "))
    vertRulerLength = float(input("Enter Vertical Ruler Length in m: "))
    pixelPerCmHorz = float(input("Enter pixels per cm - horizontal: "))
    pixelPerCmVert = float(input("Enter pixels per cm - vertical: "))

    return [leftCamPos, rightCamPos, camHeight, horzRulerLength, vertRulerLength, pixelPerCmHorz, pixelPerCmVert]
