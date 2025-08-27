import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import fluidfoam as fl ### Most Important
import scipy as sp
from matplotlib.colors import ListedColormap
import os
import io

#%matplotlib inline

plt.rcParams.update({'font.size' : 18, 'font.family' : 'Times New Roman', "text.usetex": True})
Path = '/iitgn/homedirs/in250130/ascii_pod/'
save_path = '/iitgn/homedirs/in250130/ascii_pod/'
print(Path)

Times = open(Path + 'times.txt').read().splitlines()
Snapshots = len(Times)
print(Snapshots)
print(save_path)

vel = fl.readvector(Path, time_name='latestTime', name='U', structured=False)
columns, rows = np.shape(vel.T)
print(columns, rows)

B = np.zeros((columns*rows,Snapshots)) # Matrix to store the fluctuating velocity field

# Reading the mean velocity field
Mean_vel1 = fl.readvector(Path, time_name=str(Times[0]), name='UMean', structured=False)

for i in np.arange(0,Snapshots):
    vel1 = fl.readvector(Path, time_name=str(Times[i]), name='U', structured=False)
    new_vel1 = np.reshape(vel1.T,(columns*rows,1), order='F')
    new_Mean_Vel1 = np.reshape(Mean_vel1.T,(columns*rows,1), order='F')
    MC = new_vel1 - new_Mean_Vel1
    B[:,i:i+1] = MC
print(save_path)
np.save(save_path + 'B.npy', B) ### Save the numpy file

C = np.matmul(B.T, B)/len(Times) # Autocorrelation Matrix
S, U = np.linalg.eig(C) # Eigenvalues and Eigenvectors

### POD modes
Modes = np.matmul(B,U)

### Mode Energy
res = sum([i**2 for i in S])
Energy = np.zeros((len(S),1))
for i in np.arange(0,len(S)):
    Energy[i] = S[i]**2/res



### POD Normalized Amplitudes
norms = np.linalg.norm(Modes,ord=None, axis=1)
normal_modes = np.zeros((columns*rows,Snapshots))
for i in np.arange(0,Snapshots):
    normals = np.divide(Modes.T[i], norms)
    normal_modes[:,i] = normals

Amp_test = np.matmul(normal_modes.T, B)
print(normal_modes)
print('done')







with open(Path + 'header.txt') as f:
    header="".join([f.readline() for i in range(21)])  ### 22 is number of rows

# For Footer
with open(Path + 'footer.txt') as f:
    footer="".join([f.readline() for i in range(45)])
    
saveTime = '/iitgn/homedirs/in250130/ascii_pod/'

for i in np.arange(0,10):
    Mode = np.reshape(np.real(Modes[:,i]), (columns,rows), order='F')
    np.savetxt(saveTime + 'Mode' + str(i+1), Mode, fmt='(%s %s %s)', header=header, footer=footer, comments='')
    
np.save('/iitgn/homedirs/in250130/ascii_pod/Amp_test.npy', Amp_test)
np.save('/iitgn/homedirs/in250130/ascii_pod/Energy.npy', Energy)

    
print('done1')
