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

import pyvista as pv
import numpy as np
import os

# Set your desired time
time = "26.4"  # <- You can change this to any other time folder
base_path = "/iitgn/homedirs/in250130/ascii_pod/postProcessing/surfaces1"
path_to_vtk = os.path.join(base_path, time)

# List .vtk files in the time folder
files = [f for f in os.listdir(path_to_vtk) if f.endswith('.vtk')]
print(f"VTK files in {time}:", files)

# Load the first VTK file (you can choose a specific one if needed)
vtk_file_path = os.path.join(path_to_vtk, files[0])
data = pv.read(vtk_file_path)

# Extract coordinates
points = data.points
x, y, z = points[:, 0], points[:, 1], points[:, 2]
rows, columns = np.shape(points)
print("Points shape:", rows, columns)
print("Available data arrays:", data.array_names)

# Extract Mode1 to Mode10 if they exist
modes = {}
for i in range(1, 11):
    mode_name = f"Mode{i}"
    if mode_name in data.array_names:
        modes[mode_name] = data[mode_name]
        print(f"Extracted {mode_name}")
    else:
        print(f"⚠️ {mode_name} not found in {files[0]}")

# Now modes['Mode1'], modes['Mode2'], ... contain the mode data as arrays



