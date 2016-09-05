import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10000)
size = raw_input("input size window: ")
size = int(size)

def move_window(arr,size_win):
  temp = range(len(arr)-(size_win/2)*2)
  return map(lambda x:sum(arr[x:size_win+x])/size_win,temp)


def main():
  arr = move_window(data,size)
  print arr
  fig = plt.figure()
  ax1 = fig.add_subplot(1,2,1)
  ax2 = fig.add_subplot(1,2,2)
  ax2.hist(data)
  ax1.hist(arr)
  plt.show()

if __name__ == "__main__":
  main()
