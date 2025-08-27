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
# For Header
Path = '/iitgn/homedirs/in250130/ascii_pod/'
save_path = '/iitgn/homedirs/in250130/ascii_pod/'

with open(Path + 'header.txt') as f:
    header="".join([f.readline() for i in range(21)])  ### 22 is number of rows

# For Footer
with open(Path + 'footer.txt') as f:
    footer="".join([f.readline() for i in range(45)])
    
saveTime = '/iitgn/homedirs/in250130/ascii_pod'

for i in np.arange(0,10):
    Mode = np.reshape(np.real(Modes[:,i]), (columns,rows), order='F')
    np.savetxt(saveTime + 'Mode' + str(i+1), Mode, fmt='(%s %s %s)', header=header, footer=footer, comments='')
    
    
print('done1')
