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
    sensor_h = float(input("Please enter horizontal sensor length in mm: "))
    sensor_v = float(input("Please enter vertical sensor length in mm: "))

    return [leftCamPos, rightCamPos, camHeight, focalLength, sensor_h, sensor_v]