# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:34:29 2021

@author: hihs
"""

#1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
import numpy as np
g=np.linspace(0, 20,num=21,endpoint=True)
print(g)
#2.呈上題，將以上數列取出偶數。
h=np.arange(0,20+1,2)
print(h)
#3.呈1題，將數列取出3的倍數。
i=np.arange(0,20+1,3)
print(i)