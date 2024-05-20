# Write your calc_stats function here.
import numpy as np
def calc_stats(file):
  data=np.loadtxt(file,delimiter=',')
  m=np.mean(data)
  M=np.median(data)
  m=round(m,1)
  M=round(M,1)
  return (m,M)
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('datasets/data.csv')
  print(mean)