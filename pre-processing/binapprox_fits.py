# Import the running_stats function
from helper import running_stats
from astropy.io import fits
import numpy as np
# Write your median_bins_fits and median_approx_fits here:
def median_bins_fits(dataset,B):
  mean,std=running_stats(dataset)
  dim=mean.shape
  c=np.zeros(dim)
  bins=np.zeros((dim[0],dim[1],B))
  bin_width=2*std/B
  for k in dataset:
    hdu=fits.open(k)
    data=hdu[0].data
    for i in range(dim[0]):
      for j in range(dim[1]):
        val=data[i,j]
        m=mean[i,j]
        s=std[i,j]
        if(val<(m-s)):
          c[i,j]+=1
        elif(val<(m+s) and val>=(m-s)):
          bin=int((val-(m-s))/bin_width[i,j])
          bins[i,j,bin]+=1
  return mean,std,c,bins
def median_approx_fits(dataset,B):
  mean,std,count,bins=median_bins_fits(dataset,B)
  dim=mean.shape
  mid=(len(dataset)+1)/2
  width=2*std/B
  median=np.zeros(dim)
  for i in range(dim[0]):
    for j in range(dim[1]):
      c=count[i,j]
      for b,bincount in enumerate(bins[i,j]):
        c+=bincount
        if(c>=mid):
          break
      median[i,j]=mean[i,j]-std[i,j]+width[i,j]*(b+0.5)
  return median
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with examples from the question.
  mean, std, left_bin, bins = median_bins_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  median = median_approx_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  mean, std, left_bin, bins = median_bins_fits(['image{}.fits'.format(str(i)) for i in range(11)], 4)
  median = median_approx_fits(['image{}.fits'.format(str(i)) for i in range(11)], 4)