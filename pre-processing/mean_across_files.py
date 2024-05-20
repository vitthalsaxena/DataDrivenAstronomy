# Write your mean_datasets function here
import numpy as np
def mean_datasets(datasets):
  res=[]
  x=[]
  for i in datasets:
    data=np.loadtxt(i,delimiter=',')
    x.append(data)
  for i in range(len(x[0])):
    a=[]
    for j in range(len(x[0][0])):
      sum1=0
      for k in range(len(x)):
        sum1+=x[k][i][j]
      mean=sum1/len(datasets)
      mean=round(mean,1)
      a.append(mean)
    res.append(a)
  return np.array(res)
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['datasets/data1.csv', 'datasets/data2.csv', 'datasets/data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['datasets/data4.csv', 'datasets/data5.csv', 'datasets/data6.csv']))
