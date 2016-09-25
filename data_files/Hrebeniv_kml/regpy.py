import re 
import matplotlib.pyplot as plt
import numpy as np

print 'input file name:'
path = raw_input()

f = open(path)
text = f.read()

print text

find = re.findall(r'',text)



