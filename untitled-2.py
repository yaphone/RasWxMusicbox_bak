#coding=utf-8
import os
import matplotlib.pyplot as plt
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y1 = [0.06, 0.05, 0.045, 0.04, 0.035, 0.03, 0.025, 0.02, 0.015, 0.009]
y2 = [0.035, 0.025, 0.023, 0.02, 0.018, 0.016, 0.013, 0.01, 0.007, 0.005]
    
plt.xlabel(u"域值")
plt.ylabel(u"消耗时间(秒)")
#plt.xlim(0, 100)
#plt.ylim(10, 70)
plt.plot(x, y1, "-*")
plt.plot(x, y2, "--o")
plt.legend([u'本相机耗时', u'PC端耗时'], loc='upper right')

plt.show()    
