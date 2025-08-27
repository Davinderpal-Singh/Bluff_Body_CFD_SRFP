import numpy as np

B = np.load('/iitgn/homedirs/in250130/ascii_pod/B.npy')
print("B contains NaNs:", np.isnan(B).any())



B = np.load('/iitgn/homedirs/in250130/ascii_pod/B.npy')  # shape: (space, time)
C = np.matmul(B.T, B)/B.shape[1]
S, U = np.linalg.eig(C)
Modes = np.matmul(B, U)

# Normalize each mode
norms = np.linalg.norm(Modes, axis=0)  # shape: (n_modes,)
normal_modes = Modes / norms  # shape: (space, n_modes)

# Compute amplitudes: (n_modes, time)
Amp_test = np.matmul(normal_modes.T, B)

# Save amplitudes
np.save('/iitgn/homedirs/in250130/ascii_pod/Amp_test.npy', Amp_test)

# Check again
print("Amp_test contains NaNs:", np.isnan(Amp_test).any())

