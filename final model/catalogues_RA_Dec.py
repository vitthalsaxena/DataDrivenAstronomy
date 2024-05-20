# Write your import_bss function here.
import numpy as np
def hms2dec(h,m,s):
  return 15*(h+(m/60)+(s/3600))
def dms2dec(d,m,s):
  if(d>=0):
    return (d+(m/60)+(s/3600))
  else:
    return -1*(-d+m/60+s/3600)
def import_bss():
  lst=[]
  cat=np.loadtxt('datasets/bss.dat',usecols=range(1,7))
  for i,rows in enumerate(cat,1):
    lst.append((i,hms2dec(rows[0],rows[1],rows[2]),dms2dec(rows[3],rows[4],rows[5])))
  return lst
def import_super():
  lst=[]
  cat=np.loadtxt('datasets/super.csv',delimiter=',',skiprows=1,usecols=[0,1])
  for i,rows in enumerate(cat,1):
    lst.append((i,rows[0],rows[1]))
  return lst

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)