# Vortex Shedding Frequency Analysis (Bluff Body CFD)

This script analyzes **probe velocity data** from an OpenFOAM simulation to determine the **vortex shedding frequency** and **Strouhal number** once the flow reaches a stable periodic state after the initial transient.

---

## Workflow
1. **Read Probe Data**
   - Velocity probes (`U`) are read from OpenFOAM post-processing output using `fluidfoam`.

2. **Plot Time Signal**
   - A sample probe velocity (`u`) is plotted against time.
   - The mean velocity is shown for reference.

3. **Frequency Analysis (FFT via Welch’s Method)**
   - The velocity signal is transformed to the frequency domain.
   - Power spectral density (PSD) is computed using `scipy.signal.welch`.
   - The **dominant frequency** (`f`) corresponding to vortex shedding is identified.

4. **Strouhal Number Calculation**
   - Strouhal number is computed as:
     
     St = {f * d}/{U_b}
     
     where:
     - `f`: vortex shedding frequency (Hz)  
     - `d`: bluff body characteristic length (m)  
     - `U_b`: free-stream velocity (m/s)

---

## Outputs
- **Time history plot** of probe velocity (`probeVelocity.jpeg`)  
- **Power spectral density plot** with dominant Strouhal number marked (`Power.jpeg`)  
- Printed values of:
  - Dominant Strouhal number
  - Vortex shedding frequency
  - Corresponding time period



