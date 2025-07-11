import numpy as np
import rasterio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the elevation raster
with rasterio.open("output/tex.tif") as src:
    rem = src.read(1)
    bounds = src.bounds
    width, height = src.width, src.height
    nodata = src.nodata

# Replace NoData values with NaN
if nodata is not None:
    rem = np.where(rem == nodata, np.nan, rem)

# Create coordinate grids
x = np.linspace(bounds.left, bounds.right, width)
y = np.linspace(bounds.top, bounds.bottom, height)[::-1]  # Flip Y axis
X, Y = np.meshgrid(x, y)

# Downsample for faster rendering (adjust step for quality vs speed)
step = 20
X_small = X[::step, ::step]
Y_small = Y[::step, ::step]
Z_small = rem[::step, ::step]

# Create the 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(X_small, Y_small, Z_small, cmap='RdBu', linewidth=0, antialiased=False)

# Customize the axes
ax.set_title("Relative Elevation Model (3D)")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_zlabel("Elevation (m)")

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=10, label="Elevation (m)")

# Save the plot as a PNG image
plt.tight_layout()
plt.savefig("3d_render/tex.png", dpi=300)
plt.show()