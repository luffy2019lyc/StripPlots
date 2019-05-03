"""
* date：2019/5/2 0002
* time：上午 10:24
__author__ = "lyc"

"""
import numpy as np

a = "[[34,45],[45,67],[67,89]]"
c = eval(a)
b = np.array(c)
print(b)