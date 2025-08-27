import pyvista as pv
import os
import numpy as np

PathToSurfaces = '/iitgn/homedirs/in250130/visualizationCase/postProcessing/surfaces/1/'

# Read all 10 mode files into a list
meshes = []
mode_arrays = []

for i in range(1, 11):
    filename = f"Mode{i}_xNormal.vtk"
    filepath = os.path.join(PathToSurfaces, filename)

    if not os.path.isfile(filepath):
        print(f"File {filename} not found, skipping...")
        continue

    mesh = pv.read(filepath)

    if f"Mode{i}" not in mesh.array_names:
        print(f"Mode{i} scalar not found in {filename}, skipping...")
        continue

    meshes.append(mesh)
    mode_arrays.append(mesh[f"Mode{i}"])

# Use the first mesh as base for combined plots
base_mesh = meshes[0].copy()

# Compute symmetric color range from 0 to max(abs)
global_max = max(np.max(np.abs(np.sum(mode_arrays[:n], axis=0))) for n in range(2, len(mode_arrays) + 1))
global_clim = (0, global_max)

print(f"Global color range: 0 to {global_max}")

# Generate combined mode images
for n in range(2, len(mode_arrays) + 1):
    combined_array = np.sum(mode_arrays[:n], axis=0)
    combined_name = f"Combined_{n}"
    label_title = f"Mode 1–{n}"  # Updated format

    base_mesh.point_data[combined_name] = combined_array

    plotter = pv.Plotter(off_screen=True, window_size=(1000, 320))  # Flatter figure
    plotter.add_mesh(
        base_mesh,
        scalars=combined_name,
        cmap='jet',
        show_scalar_bar=True,
        clim=global_clim,
        scalar_bar_args={
            'vertical': False,
            'title': "",
            'position_x': 0.25,
            'position_y': 0.02,
            'width': 0.5,
            'height': 0.16,  # thinner bar
            'label_font_size': 12.5,
        }
    )
    plotter.add_text(label_title, position=(10, 10), font_size=14)  # smaller font
    plotter.view_yz()
    plotter.camera.zoom(5)
    plotter.enable_parallel_projection()

    output_file = os.path.join(PathToSurfaces, f"{label_title.replace('–', '_')}.png")
    plotter.screenshot(output_file)
    plotter.close()

    print(f"✅ Saved: {output_file}")

