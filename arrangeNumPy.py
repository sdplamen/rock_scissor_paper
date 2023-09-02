import numpy as np 
 indices = np.arange(3) 
stock = np.array([10,12,25]) 
for index in indices: 
 element = stock[index] 
 print(f'Index: {index}, element: {element}')
