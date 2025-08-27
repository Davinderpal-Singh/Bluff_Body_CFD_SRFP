import pyvista as pv
import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import fluidfoam as fl ### Most Important
import scipy as sp
from matplotlib.colors import ListedColormap
import os
import io


# Path to directory with ModeX_xNormal.vtk files
PathToSurfaces = '/iitgn/homedirs/in250130/visualizationCase/postProcessing/surfaces/1/'

Files = os.listdir(PathToSurfaces)

Data = pv.read(PathToSurfaces + Files[0])
grid = Data.points
x = grid[:,0]
y = grid[:,1]
z = grid[:,2]
rows, columns = np.shape(grid)
print('rows = ', rows, 'columns = ', columns)

print(Data.array_names)

#Mode1 = Data['Mode1']
Mode2 = Data['Mode2']
Mode3 = Data['Mode3']
Mode4 = Data['Mode4']
Mode5 = Data['Mode5']
Mode6 = Data['Mode6']
Mode7 = Data['Mode7']
Mode8 = Data['Mode8']
Mode9 = Data['Mode9']
Mode10 = Data['Mode10']
