import numpy as np

def size_end(arr,size):
    size_arr = range(len(arr))
    temp = size-1
    index_arr = np.array([],dtype=np.int32)
    new_arr = np.array([],dtype=np.int32)
    # add last outing index in array 
    for i in range(temp/2):
        index_arr = np.append(index_arr,[[size_arr[:1+i]]])
        index_arr = np.append(index_arr,[[size_arr[len(arr)-temp+i:len(arr)]]])
    # make median metod with outing index
        new_arr = np.append(new_arr,np.median(arr[index_arr[:len(index_arr)]]))
        index_arr = np.array([],dtype=np.int32)
    return new_arr

def size_top(arr,size):
    size_arr = range(len(arr))
    temp = size-1
    index_arr = np.array([],dtype=np.int32)
    new_arr = np.array([],dtype=np.int32)
    for i in list(xrange(temp/2,temp)):
        index_arr = np.append(index_arr,[[size_arr[:1+i]]])
        index_arr = np.append(index_arr,[[size_arr[len(arr)-temp+i:len(arr)]]])
    # make median metod with outing index
        new_arr = np.append(new_arr,np.median(arr[index_arr[:len(index_arr)]]))
        index_arr = np.array([],dtype=np.int32)
    return new_arr[::-1]

def move_window_median(arr,size):
    iterator = range(len(arr)-size+1)
    num_arr = map(lambda x: np.median(arr[x:size+x]),iterator)
    return num_arr

def move_window_median2(arr,size):
    temp = np.copy(arr)
    iterator = range(len(arr)-size+1)
    temp[size/2:len(arr)-size/2] = map(lambda x: np.median(arr[x:size+x]),iterator)[:]
    return temp

def move_window_mean(arr,size_win):
    temp = range(len(arr)-size_win+1)
    arr = np.array(map(lambda x:np.mean(arr[x:size_win+x]),temp))
    return arr
