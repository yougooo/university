import re 
import numpy as np

data = open('20160705.kml','rU').read()

def some(str_data):
  temp = re.findall('<gx:coord>(\d.+)</gx:coord>',str_data)  
  str_temp = '' 
  for i in temp:
    str_temp = str_temp + i + ' '
  arr = re.split('\s+',str_temp)
  return arr


some(data) 
