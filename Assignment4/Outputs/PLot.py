# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:42:22 2020

@author: reetb
"""

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np


processes = [1, 2, 4, 8]
number = 11
cmap = plt.get_cmap('gnuplot')
colors = [cmap(i) for i in np.linspace(0, 1, number)]

runtime1M = [43.291197,21.153935,15.676496,13.873571]
runtime2M = [85.859164,42.978593,21.696112,23.14167]
runtime4M = [162.066315,85.726655,41.627967,38.922021]
runtime8M = [343.889206,173.504483,85.170429,52.732014]
runtime16M = [691.839992,335.708902,171.287865,94.795384]
runtime32M = [1368.873013,669.756068,345.854988,181.440915]
runtime64M = [2604.791005,1384.575076,662.883493,344.219589]
runtime128M = [5446.499479,2718.323948,1368.710998,693.063367]
runtime256M = [10824.88289,5358.829923,2714.21741,1383.696541]
runtime512M = [21291.41918,10936.97353,5503.292786,2782.430253]
runtime1B = [43130.94641,21514.51546,10910.38255,5469.153019]

fig, ax = plt.subplots()
ax.set_xscale('log', basex = 2)
ax.set_yscale('log', basey = 2)
ax.set_xticks([1, 2, 4, 8])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.plot(processes, runtime1M, '-o', label='n = 1M', color=colors[0])
ax.plot(processes, runtime2M, '-o', label='n = 2M', color=colors[1])
ax.plot(processes, runtime4M, '-o', label='n = 4M', color=colors[2])
ax.plot(processes, runtime8M, '-o', label='n = 8M', color=colors[3])
ax.plot(processes, runtime16M, '-o', label='n = 16M', color=colors[4])
ax.plot(processes, runtime32M, '-o', label='n = 32M', color=colors[5])
ax.plot(processes, runtime64M, '-o', label='n = 64M', color=colors[6])
ax.plot(processes, runtime128M, '-o', label='n = 128M', color=colors[7])
ax.plot(processes, runtime256M, '-o', label='n = 256M', color=colors[8])
ax.plot(processes, runtime512M, '-o', label='n = 512M', color=colors[9])
ax.plot(processes, runtime1B, '-o', label='n = 1B', color=colors[10])

ax.legend().remove()
plt.ylabel("Parallel Runtime (milliseconds)")
plt.xlabel("No. of threads")
plt.title("Runtime vs. #threads for different input size")
plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment4/Runtime.png', dpi = 500)



speedup1M = [1,2.046484354,2.761535295,3.120407644]
speedup2M = [1,1.997719283,3.957352543,3.710154194]
speedup4M = [1,1.89050086,3.89320754,4.16387204]
speedup8M = [1,1.982019139,4.037659667,6.521450252]
speedup16M = [1,2.060833025,4.039048487,7.298245577]
speedup32M = [1,2.043838165,3.957939196,7.544456073]
speedup64M = [1,1.881292716,3.929485396,7.567236404]
speedup128M = [1,2.003624139,3.97929109,7.858588029]
speedup256M = [1,2.020008667,3.988215111,7.823162499]
speedup512M = [1,1.946737744,3.868850888,7.65209448]
speedup1B = [1,2.004737057,3.953202027,7.886220455]



fig, ax = plt.subplots()
ax.set_xscale('log', basex = 2)
ax.set_yscale('log', basey = 2)
ax.set_xticks([1, 2, 4, 8])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.plot(processes, speedup1M, '-o', label='n = 1M', color=colors[0])
ax.plot(processes, speedup2M, '-o', label='n = 2M', color=colors[1])
ax.plot(processes, speedup4M, '-o', label='n = 4M', color=colors[2])
ax.plot(processes, speedup8M, '-o', label='n = 8M', color=colors[3])
ax.plot(processes, speedup16M, '-o', label='n = 16M', color=colors[4])
ax.plot(processes, speedup32M, '-o', label='n = 32M', color=colors[5])
ax.plot(processes, speedup64M, '-o', label='n = 64M', color=colors[6])
ax.plot(processes, speedup128M, '-o', label='n = 128M', color=colors[7])
ax.plot(processes, speedup256M, '-o', label='n = 256M', color=colors[8])
ax.plot(processes, speedup512M, '-o', label='n = 512M', color=colors[9])
ax.plot(processes, speedup1B, '-o', label='n = 1B', color=colors[10])

ax.legend().remove()
plt.ylabel("Speedup")
plt.xlabel("No. of threads")
plt.title("Speedup vs. #threads for different input size")
plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment4/Speedup.png', dpi = 500)



darts = [1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824]
precision = [0.590898,1.460709,0.404388,0.404388,0.03914,0.058568,0.00943,0.027887,0.017283,0.014045,0.007609,0.003298,0.001234,0.000096,0.000908,0.000067,0.002422,0.000479,0.000152,0.00001,0.000044]

fig, ax = plt.subplots()
ax.set_xscale('log', basex = 2)
#ax.set_xticks([4096, 2097152, 1073741824])
#ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.plot(darts, precision, '-o', color=colors[0])
#z = np.polyfit(darts, precision, 1)
#p = np.poly1d(z)
#ax.plot(darts,p(darts),"r--")

plt.ylabel("Precision (% error)")
plt.xlabel("No. of darts")
plt.title("Precision vs. #darts for p(#threads) = 8")
plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment4/Precision.png', dpi = 500)



arr = [100, 100, 100, 100]
fig, ax = plt.subplots()
ax.plot(processes, arr, label='n = 1M', color=colors[0])
ax.plot(processes, arr, label='n = 2M', color=colors[1])
ax.plot(processes, arr, label='n = 4M', color=colors[2])
ax.plot(processes, arr, label='n = 8M', color=colors[3])
ax.plot(processes, arr, label='n = 16M', color=colors[4])
ax.plot(processes, arr, label='n = 32M', color=colors[5])
ax.plot(processes, arr, label='n = 64M', color=colors[6])
ax.plot(processes, arr, label='n = 128M', color=colors[7])
ax.plot(processes, arr, label='n = 256M', color=colors[8])
ax.plot(processes, arr, label='n = 512M', color=colors[9])
ax.plot(processes, arr, label='n = 1B', color=colors[10])

plt.legend(loc="lower left", ncol=4, framealpha = 1.0)
plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment4/Legend.png', dpi = 500)