"""
To set audio to the headphone jack, call
amixer cset numid=3 1
from command line
"""

import pygame.mixer
from pygame.mixer import Sound
import numpy as np
import time
import RPi.GPIO as GPIO
from math import sin, pi

samp_freq = 44100
pygame.mixer.pre_init(frequency=samp_freq, channels=1)
pygame.mixer.init()
GPIO.setmode(GPIO.BCM)

wasPressed = 0

#initialize pins
GPIO_IN = [21]

sound1 = Sound("coin-drop-1.wav")
sound2 = [sin(i) for i in np.arange(0,2*pi,2*pi/samp_freq)]

for pin in GPIO_IN:
    GPIO.setup(pin, GPIO.IN)

while True:
    val = GPIO.input(21)

    print val
    if val == 1 and wasPressed == 0:
        wasPressed=1
        sound1.play()
        print 'played'
    elif val == 0 and wasPressed == 1:
        wasPressed = 0
        print 'released'
    time.sleep(1.0/float(samp_freq))
