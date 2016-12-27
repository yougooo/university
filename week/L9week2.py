import random

def game(size=100):
  arr = range(size+1)
  random_num = size/2
  print 'your number is {0}?'.format(random_num)
  while 1:
    asw = raw_input('enter low, higth or correct: ')
    if asw == 'low':
      arr = arr[:arr.index(random_num)]
      print arr
    elif len(arr) == 2:
      print arr
    elif asw == 'higth':
      arr = arr[arr.index(random_num):]
      print arr
    elif asw == 'correct':
      print 'game end, your number was {0}'.format(random_num)
      break      
    else:
      print 'input error'
      continue
    random_num = random.choice(arr)
    print 'your number is {0}?'.format(random_num)

game()
