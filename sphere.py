# inspiration code for Python Unit Testing Project

import math

def surfaceArea():
    SA = 4 * math.pi*(r*r)
    return SA

def volume(rad):
    volume = (4/3) * math.pi * (rad*rad*rad)
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))

    print("\nThe Volume of a Sphere = ", volume(radius))

if __name__ == '__main__':
    prompt()
