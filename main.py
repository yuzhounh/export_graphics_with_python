import os
import numpy as np
import matplotlib.pyplot as plt
from export_graphics import (
    save_with_pillow,
    save_with_opencv,
    save_with_matplotlib,
    save_with_skimage,
    save_with_imageio
)

def create_sample_image():
    """Create a sample image for testing."""
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title("Sample Sine Wave")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    return plt.gcf()

def main():
    base_path = "saved_images"
    os.makedirs(base_path, exist_ok=True)
    
    # Create a sample image
    figure = create_sample_image()
    
    # Set DPI
    dpi = 300
    
    # Save using different methods
    save_with_pillow(figure, base_path, dpi)
    save_with_opencv(figure, base_path, dpi)
    save_with_matplotlib(figure, base_path, dpi)
    save_with_skimage(figure, base_path, dpi)
    save_with_imageio(figure, base_path, dpi)
    
    plt.close(figure)

if __name__ == "__main__":
    main()