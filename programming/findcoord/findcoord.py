import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns; sns.set()
import re

#test_path = r'/home/alex/Download/files/20160705.kml'
f = open('20160705.kml','rU')
data = f.read()

def data_to_arr(st):
  st = re.findall('<gx:coord>(\d.+) (\d.+) (\d.+)</gx:coord>',st)
  st = np.array(st,dtype=np.float32)
  return pd.DataFrame(st,columns=['Lon','Lat','Height'])

def move_median(arr):
  temp = np.array(map(lambda x: np.median(arr[x:5+x]),range(len(arr)-4)))
  arr[2:len(arr)-2] = temp
  return arr

def main():
  grap = data_to_arr(data)
  fig = plt.figure()
  ax = fig.add_subplot(1,2,1)
  ax1 = fig.add_subplot(1,2,2)
  ax.plot(move_median(grap.Height))
  ax1.scatter(move_median(grap.Lon),move_median(grap.Lat), s=100, c='green', alpha=0.5)
  plt.show()

if __name__ == '__main__':
  main()
