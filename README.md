# Python Image Export Comparison

This project compares different methods and libraries for exporting images in various formats and resolutions in Python.

## Description

This script demonstrates how to save images using different Python libraries:
1. Pillow (PIL)
2. OpenCV (cv2)
3. Matplotlib
4. scikit-image
5. imageio v3

It creates a sample sine wave plot and saves it in multiple formats using each method, allowing for a comparison of the output quality, file size, and supported formats.

## Getting Started

### Dependencies

* Python 3.x
* numpy
* matplotlib
* Pillow
* OpenCV
* scikit-image
* imageio

Install the required packages using:
```
pip install numpy matplotlib pillow opencv-python scikit-image imageio
```

### Executing program

* Run the main script:
```
python main.py
```


## Output

The script will create a `saved_images` directory with subdirectories for each method:

1. `method_1_pillow`
2. `method_2_opencv`
3. `method_3_matplotlib`
4. `method_4_skimage`
5. `method_5_imageio`

Each subdirectory will contain the sample image saved in various formats supported by that method.

### Supported Formats

- **Pillow**: eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff, webp
- **OpenCV**: jpeg, jpg, png, tif, tiff, webp, bmp, ppm, pbm, pgm
- **Matplotlib**: eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff, webp
- **scikit-image**: jpeg, jpg, pdf, pgf, png, raw, rgba, svg, svgz, tif, tiff, webp, bmp, gif, ppm, pgm
- **imageio**: jpeg, jpg, pdf, pgf, png, raw, rgba, svg, svgz, tif, tiff, webp, bmp, gif, ppm, pgm

## Acknowledgments

* [Matplotlib](https://matplotlib.org/)
* [Pillow](https://python-pillow.org/)
* [OpenCV](https://opencv.org/)
* [scikit-image](https://scikit-image.org/)
* [imageio](https://imageio.readthedocs.io/)

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).

## Contact

Jing Wang: wangjing@xynu.edu.cn

Project Link: [https://github.com/yuzhounh/python-image-export-comparison](https://github.com/yuzhounh/python-image-export-comparison)