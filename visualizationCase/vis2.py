import pyvista as pv
import os

PathToSurfaces = '/iitgn/homedirs/in250130/visualizationCase/postProcessing/surfaces/1/'

# Loop through Mode1 to Mode10
for i in range(1, 11):
    filename = f"Mode{i}_xNormal.vtk"
    filepath = os.path.join(PathToSurfaces, filename)

    if not os.path.isfile(filepath):
        print(f"File {filename} not found, skipping...")
        continue

    Data = pv.read(filepath)
    print(f"Reading {filename}, Arrays = {Data.array_names}")

    if len(Data.array_names) == 0:
        print(f"No scalar fields found in {filename}")
        continue

    scalar_name = Data.array_names[0]

    # Set up headless plot
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(Data, scalars=scalar_name, cmap='jet', show_scalar_bar=True)
    plotter.add_title(scalar_name)

    # Set YZ plane view
    plotter.view_yz()
    plotter.camera.zoom(1.2)  # optional zoom
    plotter.enable_parallel_projection()  # orthographic view

    # Save image
    output_file = os.path.join(PathToSurfaces, f"{scalar_name}.png")
    plotter.screenshot(output_file)
    plotter.close()

    print(f"Saved image: {output_file}")

