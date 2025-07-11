import plotly.graph_objects as go
import numpy as np
import rasterio

#load rem
with rasterio.open("hood.tif") as src:
    rem = src.read(1)
    bounds = src.bounds
    res = src.res
    width, height = src.width, src.height



#generate x and y grids
x = np.linspace(bounds.left, bounds.right, width)
y = np.linspace(bounds.top, bounds.bottom, height)[::-1]  # reverse y to match rasterio's coordinate system
X, Y = np.meshgrid(x, y)

# plot rem as 3d surface
fig = go.Figure(data=[go.Surface(z= rem, x= X, y=Y, colorscale='RdBu')])

fig.update_layout(
    title= "Relative Elevation Model (3d)",
    scene= dict(
        xaxis_title= 'Longitude',
        yaxis_title= 'Latitude',
        zaxis_title= 'Relative Elevation (m)',
        aspectratio= dict(x= 1, y= 1, z= 0.2),
    ),
    height= 700,
    margin = dict(l= 0, r= 0, t= 30, b= 0)
)

#fig.write_html("rem_3d.html")
fig.show()