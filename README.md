# Volvo Bluff Body CFD – SRFP Project

This repository contains simulation cases, post-processing scripts, and results from the **Summer Research Fellowship Program (SRFP)** project on **Modeling of Airflow in the Volvo Bluff Body Experiment: Model Validation and POD (Proper Orthogonal Decomposition)**.

---

## Project Overview  
This project focuses on:
- Performing CFD simulations using **OpenFOAM** and Validation of results against experimental data (https://community.apan.org/wg/afrlcg/mvpws/p/experimental-data  ....non-reacting case) .
- Performing **POD analysis** to extract dominant flow modes.
- Visualizing energy contributiion of dominant modes and reconstruction of flow.
-LES simulations has been also performed.
-Adaptive Mesh Refinement with k-ω SST case has been also tried


## Simulations Performed

- **RANS simulations**  
  - k-ε model  
  - k-ω SST model  

- **LES simulations**  
  - WALE  
  - Smagorinsky  
  - Dynamic k-equation  

- **Adaptive Mesh Refinement (AMR)**  
  - Applied with **k-ω SST**  
  - Critical regions refined using **vorticity magnitude** (defined via function object, since AMR works only on scalar fields).  

All setups are included with **required case files** and **job submission scripts**.


## 📂 Repository Structure
├── amr/ # AMR case with k-omega SST
├── ascii_pod
├── dynamicKEqn/ # LES with dynamic k-equation model
├── FFT
├── python_post_processing_files
├── results
├── smagorinsky/ # LES with Smagorinsky model
├── wale/ # LES with WALE model
├── visualisationCase
├── transient2_kEpsilon/ # RANS with k-ε model
├── new_kEp/ # Additional RANS (k-ε) results
├── results/ # POD results and visualizations
├── SRFP_report.pdf # Final project report
├── SRFP_PPT.pdf # project Presentation
├── cluster and OpenFOAM commads.doc # Cluster and OpenFOAM commands
├── vtascii4.msh (coarse mesh-3d)
├── vtascii2.msh (fine mesh-3d)


## NOTE
for data visualisation purposes , separate directories visualisationCase  and ascii_pod to be created \by copying 0 , constant and system files , and making new time directory named 1 additionally
more explained in this article(https://goswami-13.github.io/posts/2024/04/blog-post-24/)

## Resources
- **Experimental Data:** [MVP Workshop – Non-reacting case](https://community.apan.org/wg/afrlcg/mvpws/p/experimental-data)  
- **POD Reference:** [Blog on Method of Snapshots](https://goswami-13.github.io/posts/2024/06/blog-post-23/)  
- **AMR Implementation:** [GradientAMR (GitHub)](https://github.com/nicolasbadano/GradientAMR)

