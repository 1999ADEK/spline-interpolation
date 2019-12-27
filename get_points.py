# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 09:33:27 2019

@author: ADEK
"""

import matplotlib.pyplot as plt

file_name = input("Filename:")

fig, ax = plt.subplots()
ax.axis('equal')
pts = plt.ginput(-1, 0)
n = len(pts)

with open(file_name, 'w+') as f:
    f.write('%d\n' % n)
    for (x, y) in pts:
        f.write('%f %f\n' % (x, y))