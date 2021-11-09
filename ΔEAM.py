import os, sys
import numpy as np
from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie1976
from read import reader
from read import check

#Take RGB Val, IE: 255,255,255
#Get difference of this from the middle pixel and multiply it by 2.55
#Do the same for all pixels in radius
#Get all the values
#Get means of all of them
#The mean is the total rgb value


reader(input("Give name of file (relative) to ΔEAMify: "))
