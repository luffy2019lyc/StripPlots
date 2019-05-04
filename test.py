"""
* date：2019/5/2 0002
* time：上午 10:24
__author__ = "lyc"

"""
import numpy as np

a = "[[34,45],[45,67],[67,89]]"
c = eval(a)
b = np.array(c)
# print(b)

d = {"a":{'b':'b','c':'c','d':[3,4]},"b":{'b':'b','c':'c','d':[3,4]}}
# d = np.array([[3,4],[5,6]])
# d1 = np.array([[34,44],[5,6]])
# d = np.vstack((d, d1))
for k,v in d.items():
    print(k,v)
print(d["a"]["b"])
# ok
