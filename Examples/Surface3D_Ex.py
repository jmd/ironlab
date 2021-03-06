from ironplot import *
from math import *
x = [i*0.2 for i in range(75)]
y = [i*0.2 for i in range(50)]
window(5)
tab(1)
z = [[yj**2 * sin(xi) for yj in y] for xi in x]  
# or could also have:
#z = [yj**2 * sin(xi) for yj in y for xi in x]  
plot3d(x, y, z)
p3d = currentplot()
tab(2)
image(x, y, z)

# customize the plot:
axes = p3d.Viewport3D.Axes
axes.XAxes.AxisLabels.Text = "New X label"
axes.YAxes.AxisLabels.Text = "New Y label"
axes.ZAxes.AxisLabels.Text = "New Z label"
axes.XAxes.TickLength = 0.05 # as fraction of axis length
#axes.LineThickness = 1