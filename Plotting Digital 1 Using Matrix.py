# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 18:39:55 2022

@author: anees
"""

import matplotlib.pyplot as plt

data = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,1,1,1,1,1,0]]

plt.imshow(data, cmap='gray')
plt.show()