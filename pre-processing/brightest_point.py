# Write your load_fits function here.
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
def load_fits(image):
  hdu=fits.open(image)
  d=hdu[0].data
  return np.unravel_index(np.argmax(d, axis=None), d.shape)
if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('datasets/image1.fits')
  print(bright)
  # You can also confirm your result visually:
  hdulist = fits.open('datasets/image1.fits')
  data = hdulist[0].data
  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()