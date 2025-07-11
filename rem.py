import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# s1 load dem
dem_path = "input/mthood.tif"
with rasterio.open(dem_path) as src:
    dem = src.read(1, masked= True)
    profile = src.profile


#s2 smooth dem
smoothed_dem = gaussian_filter(dem.filled(0), sigma= 10)

#s3 calculate rem
rem = dem - smoothed_dem

# s4 visualization 
fig, ax = plt.subplots(1, 3, figsize= (18, 6))
show(dem, ax= ax[0], title = "Original DEM", cmap= 'terrain')
show(smoothed_dem, ax= ax[1], title= "Smoothed surface", cmap= 'terrain')
show(rem, ax= ax[2], title= "Relative Elevation Model", cmap= 'RdBu')

plt.tight_layout()
plt.show()

#save rem to a new Geotiff
out_path = "output/hood.tif"
profile.update(dtype= rasterio.float32)

with rasterio.open(out_path, 'w', **profile) as dst:
    dst.write(rem.astype(rasterio.float32), 1)