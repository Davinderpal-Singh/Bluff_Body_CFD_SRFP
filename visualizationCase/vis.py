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

# Base mesh from Mode1 file
base_file = os.path.join(PathToSurfaces, 'Mode1_xNormal.vtk')
mesh = pv.read(base_file)

# Print and handle unknown array name in Mode1
existing_arrays = mesh.array_names
if len(existing_arrays) == 1:
    mesh.point_data["Mode1"] = mesh[existing_arrays[0]]
    mesh.point_data.remove(existing_arrays[0])
else:
    print("⚠️ Unexpected number of arrays in Mode1_xNormal.vtk:", existing_arrays)

# Read Mode2 to Mode10 and attach them
for i in range(2, 11):
    filename = f"Mode{i}_xNormal.vtk"
    filepath = os.path.join(PathToSurfaces, filename)
    if os.path.exists(filepath):
        d = pv.read(filepath)
        arrs = d.array_names
        if len(arrs) == 1:
            mesh.point_data[f"Mode{i}"] = d[arrs[0]]
            print(f"✅ Mode{i} loaded from {filename}")
        else:
            print(f"⚠️ Unexpected arrays in {filename}: {arrs}")
    else:
        print(f"❌ File {filename} not found")

# Show final status
print("✅ Final array names in mesh:", mesh.array_names)

# Save if needed
mesh.save("allModes.vtk")

# Now safely extract
Mode1 = mesh['Mode1']
Mode2 = mesh['Mode2']
Mode3 = mesh['Mode3']
Mode4 = mesh['Mode4']
Mode5 = mesh['Mode5']
Mode6 = mesh['Mode6']
Mode7 = mesh['Mode7']
Mode8 = mesh['Mode8']
Mode9 = mesh['Mode9']
Mode10 = mesh['Mode10']


