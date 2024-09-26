import matplotlib.pyplot as plt
import numpy as np
import os
from export_graphics import export_graphics

# Create a simple line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Export graphics
figures_dir = 'figures'  # Figures directory
base_filename = 'figure_1'  # Define base filename
export_graphics(figures_dir, base_filename)