## Scripts

### vis.py
This script uses **PyVista** to visualize POD mode data stored in `.vtk` files generated during post-processing.  

Key steps:
- Points to a given simulation time directory inside `postProcessing/surfaces1`.  
- Lists all `.vtk` files available at that time step.  
- Reads the first `.vtk` file and prints available arrays.  
- Extracts **Mode1–Mode10** if present in the dataset.  

Use this script to quickly verify which POD modes are written into the `.vtk` files and to load them into a Python/PyVista environment for custom visualization.

---

### py2.py
This script prepares **OpenFOAM-compatible ASCII files** of the first 10 POD modes.  

Key steps:
- Reads the stored OpenFOAM `header.txt` and `footer.txt` to preserve file format.  
- Reshapes each POD mode into the correct mesh structure.  
- Saves the first 10 modes (`Mode1` … `Mode10`) as ASCII files with headers/footers.  

These files can be directly loaded into **ParaView** (via `foamToVTK` or as ASCII input) to visualize POD mode structures over the computational mesh.

---

### Workflow Connection
- `podScript.py` → generates `B.npy`, `Energy.npy`, `Amp_test.npy`, and raw mode arrays.  
- `energy.py` → processes energies and amplitudes, outputs plots and animation.  
- `py2.py` → converts raw POD modes into **OpenFOAM-style ASCII files** for visualization.  
- `vis.py` → reads `.vtk` outputs (from OpenFOAM postProcessing) and extracts available POD mode fields for further analysis/plots.  

Together, these scripts provide a complete chain: **CFD simulation → POD decomposition → Energy analysis → Mode file export → Visualization**.  

### podScript.py
This Python script performs **Proper Orthogonal Decomposition (POD)** on velocity field data extracted from OpenFOAM simulations. It uses the `fluidfoam` library to read velocity vectors from case directories and constructs the fluctuation matrix required for POD.

Key steps:
- Reads time snapshots of velocity (`U`) and mean velocity (`UMean`) from OpenFOAM ASCII output.
- Constructs the data matrix **B** containing velocity fluctuations across all snapshots.
- Forms the autocorrelation matrix and computes eigenvalues/eigenvectors.
- Extracts POD modes, normalized amplitudes, and modal energy content.
- Saves:
  - **B.npy** (fluctuation matrix)  
  - **Energy.npy** (normalized energy of modes)  
  - **Amp_test.npy** (modal amplitudes)  
  - Individual **Mode files** (Mode1, Mode2, …) in ASCII format with OpenFOAM-compatible headers/footers.

These outputs are used in post-processing (see the `results/` folder) to generate energy plots, mode visualizations, and animations.


### energy.py
This script analyzes and visualizes the **energy distribution of POD modes** and their temporal amplitudes. It works with the outputs from `podScript.py`.

Key steps:
- Loads `B.npy`, `Amp_test.npy`, and `times.txt` generated during POD.  
- Computes eigenvalues of the correlation matrix to determine POD mode energy.  
- Saves normalized **Energy.npy** and cumulative energy distribution.  
- Generates plots:
  - `energy_plot.png` – bar plot of mode energy (log scale).  
  - `cumulative_energy.png` – cumulative energy vs number of modes.  
  - `amplitudes_vs_time.png` – time evolution of amplitudes for first 10 modes.  
  - `amplitudes_subplots.png` – individual amplitude plots (first 10 modes).  
  - `amplitudes_animation.gif` – animated time evolution of first 10 modes.  
- Reports the **number of modes required** to capture thresholds of 90%, 95%, 99%, 99.5%, and 99.9% of total energy.



  

