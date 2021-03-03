# Name: Prakul Tandon
# Roll Number: 2019BCS-041
import numpy as np
import math

input_coordinates = np.array(list(map(float, input( "Enter coordinates of initial"
    " point(separated by spaces): ").split()))).reshape((3, 1))

angle_x = np.deg2rad(float(input("Enter degree of rotation about X axis: ")))
angle_y = np.deg2rad(float(input("Enter degree of rotation about Y axis: ")))
angle_z = np.deg2rad(float(input("Enter degree of rotation about Z axis: ")))

rotation_x = np.array([[1, 0, 0],[0, math.cos(angle_x), -math.sin(angle_x)],[0, math.sin(angle_x), math.cos(angle_x)]])

rotation_y = np.array([[math.cos(angle_y), 0, math.sin(angle_y)],[0, 1, 0],[-math.sin(angle_y), 0, math.cos(angle_y)]])

rotation_z = np.array([[math.cos(angle_z),  -math.sin(angle_z), 0],[math.sin(angle_z), math.cos(angle_z), 0],[0, 0, 1]])

rotation_matrix= rotation_x @ rotation_y @ rotation_z
print("New coordinates are: ", rotation_matrix@input_coordinates)
