# Write your mean_fits function here:
import numpy as np
from astropy.io import fits
def mean_fits(datasets):
  hdu=fits.open(datasets[0])
  d=hdu[0].data
  hdu.close()
  for i in range(1,len(datasets)):
    hdu=fits.open(datasets[i])
    d+=hdu[0].data
    hdu.close()
  mean=d/len(datasets)
  return mean 
    
    
if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100,100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()