import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
from skimage import io
import imageio.v3 as iio

def save_with_pillow(image, base_path, dpi):
    """Save image using Pillow (PIL)."""
    print("\nUsing Pillow method:")
    folder = os.path.join(base_path, "method_1_pillow")
    os.makedirs(folder, exist_ok=True)
    
    formats = ['eps', 'jpeg', 'jpg', 'pdf', 'pgf', 'png', 'ps', 'raw', 'rgba', 'svg', 'svgz', 'tif', 'tiff', 'webp']
    for fmt in formats:
        filename = os.path.join(folder, f"sample_image.{fmt}")
        image.savefig(filename, dpi=dpi)
        
        # Skip DPI check for formats without DPI
        if fmt in ['eps', 'pdf', 'pgf', 'ps', 'raw', 'rgba', 'svg', 'svgz']:
            print(f"Pillow: Successfully saved {filename}")
            continue
        
        # Read the saved image and get DPI using Pillow
        try:
            with Image.open(filename) as img:
                img_dpi = img.info.get('dpi', (None, None))[0]
                if img_dpi is not None:
                    img_dpi = round(img_dpi)
            print(f"Pillow: Successfully saved {filename} (DPI: {img_dpi})")
        except Exception as e:
            print(f"Pillow: Successfully saved {filename} (Unable to read DPI: {str(e)})")
    
    print(f"Pillow: Saved {len(formats)} formats in {folder}")

def save_with_opencv(image, base_path, dpi):
    """Save image using OpenCV (cv2)."""
    print("\nUsing OpenCV method:")
    folder = os.path.join(base_path, "method_2_opencv")
    os.makedirs(folder, exist_ok=True)
    
    # Convert matplotlib figure to numpy array
    fig = plt.gcf()
    fig.canvas.draw()
    img_array = np.array(fig.canvas.renderer.buffer_rgba())
    
    # Calculate new dimensions based on DPI
    height, width = img_array.shape[:2]
    new_height = int(height * dpi / 100)
    new_width = int(width * dpi / 100)
    
    formats = ['jpeg', 'jpg', 'png', 'tif', 'tiff', 'webp', 'bmp', 'ppm']
    for fmt in formats:
        filename = os.path.join(folder, f"sample_image.{fmt}")
        resized_img = cv2.resize(cv2.cvtColor(img_array, cv2.COLOR_RGBA2BGR), (new_width, new_height))
        cv2.imwrite(filename, resized_img)
        
        # Read the saved image and get DPI using OpenCV
        try:
            img = cv2.imread(filename)
            height, width = img.shape[:2]
            img_dpi = round((width / (fig.get_size_inches()[0])))
            print(f"OpenCV: Successfully saved {filename} (DPI: {img_dpi})")
        except Exception as e:
            print(f"OpenCV: Successfully saved {filename} (Unable to read DPI: {str(e)})")
    
    print(f"OpenCV: Saved {len(formats)} formats in {folder}")

def save_with_matplotlib(figure, base_path, dpi):
    """Save image using Matplotlib."""
    print("\nUsing Matplotlib method:")
    folder = os.path.join(base_path, "method_3_matplotlib")
    os.makedirs(folder, exist_ok=True)
    
    formats = ['eps', 'jpeg', 'jpg', 'pdf', 'pgf', 'png', 'ps', 'raw', 'rgba', 'svg', 'svgz', 'tif', 'tiff', 'webp']
    for fmt in formats:
        filename = os.path.join(folder, f"sample_image.{fmt}")
        figure.savefig(filename, format=fmt, dpi=dpi, bbox_inches='tight')
        
        # Skip DPI check for formats without DPI
        if fmt in ['eps', 'pdf', 'pgf', 'ps', 'raw', 'rgba', 'svg', 'svgz']:
            print(f"Matplotlib: Successfully saved {filename}")
            continue
        
        # Read the saved image and get DPI using Pillow
        try:
            with Image.open(filename) as img:
                img_dpi = img.info.get('dpi', (None, None))[0]
                if img_dpi is not None:
                    img_dpi = round(img_dpi)
                    print(f"Matplotlib: Successfully saved {filename} (DPI: {img_dpi})")
                else:
                    print(f"Matplotlib: Successfully saved {filename} (DPI: None)")
        except Exception as e:
            print(f"Matplotlib: Successfully saved {filename} (Unable to read DPI: {str(e)})")
    
    print(f"Matplotlib: Saved {len(formats)} formats in {folder}")

def save_with_skimage(image, base_path, dpi):
    """Save image using scikit-image."""
    print("\nUsing scikit-image method:")
    folder = os.path.join(base_path, "method_4_skimage")
    os.makedirs(folder, exist_ok=True)
    
    # Convert matplotlib figure to numpy array
    fig = plt.gcf()
    fig.canvas.draw()
    img_array = np.array(fig.canvas.renderer.buffer_rgba())
    
    # Calculate new dimensions based on DPI
    height, width = img_array.shape[:2]
    new_height = int(height * dpi / 100)
    new_width = int(width * dpi / 100)
    
    formats = ['jpeg', 'jpg', 'png', 'tif', 'tiff', 'webp', 'bmp', 'gif', 'ppm', 'pgm']
    for fmt in formats:
        filename = os.path.join(folder, f"sample_image.{fmt}")
        resized_img = cv2.resize(img_array, (new_width, new_height))
        
        # Convert RGBA to RGB for formats that don't support alpha channel
        if fmt in ['jpg', 'jpeg']:
            resized_img = cv2.cvtColor(resized_img, cv2.COLOR_RGBA2RGB)
        
        io.imsave(filename, resized_img)
        
        # Read the saved image and get DPI using scikit-image
        try:
            img = io.imread(filename)
            img_dpi = round((img.shape[1] / (fig.get_size_inches()[0])))
            print(f"scikit-image: Successfully saved {filename} (DPI: {img_dpi})")
        except Exception as e:
            print(f"scikit-image: Successfully saved {filename} (Unable to read DPI: {str(e)})")
    
    print(f"scikit-image: Saved {len(formats)} formats in {folder}")

def save_with_imageio(image, base_path, dpi):
    """Save image using imageio v3."""
    print("\nUsing imageio v3 method:")
    folder = os.path.join(base_path, "method_5_imageio")
    os.makedirs(folder, exist_ok=True)
    
    # Convert matplotlib figure to numpy array
    fig = plt.gcf()
    fig.canvas.draw()
    img_array = np.array(fig.canvas.renderer.buffer_rgba())
    
    # Calculate new dimensions based on DPI
    height, width = img_array.shape[:2]
    new_height = int(height * dpi / 100)
    new_width = int(width * dpi / 100)
    
    formats = ['jpeg', 'jpg', 'png', 'tif', 'tiff', 'webp', 'bmp', 'gif', 'ppm', 'pgm']
    for fmt in formats:
        filename = os.path.join(folder, f"sample_image.{fmt}")
        resized_img = cv2.resize(img_array, (new_width, new_height))
        
        # Convert RGBA to RGB for formats that don't support alpha channel
        if fmt in ['jpg', 'jpeg']:
            resized_img = cv2.cvtColor(resized_img, cv2.COLOR_RGBA2RGB)
        
        iio.imwrite(filename, resized_img)
        
        # Read the saved image and get DPI using imageio v3
        try:
            img = iio.imread(filename)
            img_dpi = round((img.shape[1] / (fig.get_size_inches()[0])))
            print(f"imageio v3: Successfully saved {filename} (DPI: {img_dpi})")
        except Exception as e:
            print(f"imageio v3: Successfully saved {filename} (Unable to read DPI: {str(e)})")
    
    print(f"imageio v3: Saved {len(formats)} formats in {folder}")
