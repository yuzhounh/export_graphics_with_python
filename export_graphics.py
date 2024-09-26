def export_graphics(figures_dir, base_filename):
    import matplotlib.pyplot as plt
    import numpy as np
    import os

    # Create 'figures' directory if it doesn't exist
    os.makedirs(figures_dir, exist_ok=True)

    # List of supported file formats to save
    formats = ['eps', 'jpeg', 'jpg', 'pdf', 'pgf', 'png', 'ps', 'raw', 'rgba', 'svg', 'svgz', 'tif', 'tiff', 'webp']

    # Save the figure in each supported format
    for fmt in formats:
        plt.savefig(os.path.join(figures_dir, f'{base_filename}.{fmt}'), 
                    bbox_inches='tight', 
                    dpi=300 if fmt in ['png', 'jpg', 'jpeg', 'tif', 'tiff'] else None)

    print(f"Figure saved in {len(formats)} different formats in the '{figures_dir}' directory.")

    # Close the plot to free up memory
    plt.close()