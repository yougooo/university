import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(1000)
size = int(raw_input("input size window: "))

def move_window(arr,size_win):
  temp = range(len(arr)-(size_win/2)*2)
  return map(lambda x:np.average(arr[x:size_win+x]),temp)


def main():
  arr = move_window(data,size)
  print arr
  fig = plt.figure()
  ax1 = fig.add_subplot(1,2,1)
  ax2 = fig.add_subplot(1,2,2)
  ax2.plot(data)
  ax1.plot(arr)
  plt.show()

if __name__ == "__main__":
  main()
