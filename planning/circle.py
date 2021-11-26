#!/usr/bin/python3
import math

def getPointX(angleInDegrees, radius, centerX):
    return centerX + (radius * math.cos(math.radians(angleInDegrees)))

def getPointY(angleInDegrees, radius, centerY):
    return centerY + (radius * math.sin(math.radians(angleInDegrees)))

if __name__ == '__main__':
    NUMBER_OF_LEDS_IN_CIRCLE = 32
    RADIUS = 45
    ANGLE = 11.25
    
    STARTANGLE = 270
    
    CENTERX=100
    CENTERY=100
    
    print("Number of LEDs in circle: ", NUMBER_OF_LEDS_IN_CIRCLE)
    print("Radius of circle: ", RADIUS)
    print("Angle between LEDs: ", ANGLE)
    print("circle center x: ", CENTERX)
    print("circle center y: ", CENTERY)
    print()
    
    text="LED Nr. {} \tx: {:.3f},\ty: {:.3f}, \tangle: {:.3f}"
    
    for index in range(NUMBER_OF_LEDS_IN_CIRCLE):
        angle = -ANGLE * (index + 1)
        valueX = getPointX(angle, RADIUS, CENTERX)
        valueY = getPointY(angle, RADIUS, CENTERY)
        print(text.format(index + 1, valueX, valueY, (STARTANGLE - angle) % 360))
