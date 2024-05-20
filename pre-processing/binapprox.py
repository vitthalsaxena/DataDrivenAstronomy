# Write your median_bins and median_approx functions here.
import numpy as np
def median_bins(dataset,B):
  mean=np.mean(dataset)
  std=np.std(dataset)
  c=0
  bins=np.zeros(B)
  bin_width=2*std/B
  for i in dataset:
    if(i<(mean-std)):
      c+=1
    elif(i<(mean+std)):
      bin=int((i-(mean-std))/bin_width)
      bins[bin]+=1
  return mean,std,c,bins

def median_approx(dataset,B):
  mean,std,count,bins=median_bins(dataset,B)
  mid=(len(dataset)+1)/2
  for b,bincount in enumerate(bins):
    count+=bincount
    if(count>=mid):
      break
  width=2*std/B
  median=mean-std+width*(b+0.5)
  return median
# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
