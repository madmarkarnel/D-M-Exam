# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:44:35 2021

@author: MAD
"""

import serial
import numpy as np
import pandas as pd
import datetime as dt

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
x_len = 200         # Number of points to display
y_range = [-10000, 10000]  # Range of possible Y values to display

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 200))
xa = [0] * x_len
ax.set_ylim(y_range)

#xa = []
#ya = []
#za = []
#ts = []

# Create a blank line. We will update the line in animate
line, = ax.plot(xs, xa)

plt.title('Realtime Plotter')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

ser = serial.Serial('COM13', 115200, timeout = 1) #set the COM port of the receiver
print ("Starting . . .")

def animate(i, xa):

    sRead = ser.readline().decode('ascii', 'replace')
    # x, y, z
    accel = sRead.strip('\r\n').split(',')

    # Add y to list
    xa.append(accel[0])

    # Limit y list to set number of items
    xa = xa[-x_len:]

    # Update line with new Y values
    line.set_ydata(xa)

    return line,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(xa,),
    interval=50,
    blit=True)
plt.show()

'''
# This function is called periodically from FuncAnimation
def animate(i, ts, xa):
    
    sRead = ser.readline().decode('ascii', 'replace')
    accel = sRead.strip('\r\n').split(',')
    
    # Add x and y to lists
    xa.append(accel[0])
    ya.append(accel[1])
    za.append(accel[2])
    ts.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    
    # Limit x and y lists to 20 items
    xa = xa[-20:]
    #ya = ya[-20:]
    ts = ts[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(ts, xa)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Realtime Plotter')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(ts, xa), interval=1000)
plt.show()
'''

'''
while True:
    sRead = ser.readline().decode('ascii', 'replace')
    accel = sRead.strip('\r\n').split(',')
    
    #xa.append(accel[0])
    #ya.append(accel[1])
    #za.append(accel[2])
    #print(xa)
    
    xa = accel[0]
    ya = accel[1]
    za = accel[2]

    theta_xz = np.arctan([za,(np.sqrt(xa**2 + ya**2))])
    theta_xy = np.arctan([ya,(np.sqrt(xa**2 + za**2))])

    xz = seg_len * np.sin(theta_xz)
    xy = seg_len * np.sin(theta_xy)
    
    print(xz)
'''