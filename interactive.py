__author__ = 'jean'

from interactive_model import *
from input_command import *

modes = ['I', 'F', 'Q']
print['Enter mode for operation']
print["you can enter 'i' for interactive_model, 'f' for file_model and 'q' for to quit"]

try:
    mode = input()
    mode = str.capitalize(mode)
    if mode == 'i':
        print("Welcome to Shapes and Solids calculator")
        Shapes = ['Circle', 'Rectangle', 'Triangle', 'parallelogram', 'Trapezoid']
        Solids = ['Sphere', 'Cube', 'Cone', 'Cylinder']
        option = ['Solids', 'Shapes', 'Quit']