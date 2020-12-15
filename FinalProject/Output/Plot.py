# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:02:05 2020

@author: reetb
"""

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np

file = 4                    #1: f, 2: g, 3: b, 4: n
processes = [1, 2, 4, 8]

number = 6
cmap = plt.get_cmap('gnuplot')
colors = [cmap(i) for i in np.linspace(0, 1, number)]

if file == 1:
    runtime8 = [23.227,12.645,6.8,4.38]
    runtime16 = [43.9,23.85,12.56,9.17]
    runtime32 = [85.486,45.97,23.71,17.73]
    runtime64 = [166.11,90.48,46.55,25.57]
    runtime128 = [332.96,179.632,91.653,47.253]
    runtime256 = [660.07,356.969,183.56,93.6]
if file == 2:
    runtime8 = [6938.72,3541.97,1792.43,913.365]
    runtime16 = [13305.9,6740.93,3413.07,1737.53]
    runtime32 = [25981.6,13130.8,6664.24,3415.02]
    runtime64 = [51180.8,25895.3,13081.3,6777.8]
    runtime128 = [101448,51418.7,26031.4,13473]
    runtime256 = [202536,102936,52215.2,26972.2]
if file == 3:
    runtime8 = [4577.61,2317.21,1172.04,594.1]
    runtime16 = [8832.89,4446.46,2275.67,1160.23]
    runtime32 = [17397.8,8874.32,4492.74,2309]
    runtime64 = [34431.9,17639.7,8913.41,4589.33]
    runtime128 = [68574.3,35375.4,17712.7,9126.5]
    runtime256 = [137004,69135.6,35388.4,18315.8]
if file == 4:    
    runtime8 = [2111.2,1097.49,561.671,285.957]
    runtime16 = [4074.68,2101.54,1077.48,545.538]
    runtime32 = [7921.8,4116.47,2100.58,1075.37]
    runtime64 = [15649.6,8140.54,4145.36,2128.36]
    runtime128 = [31313.3,16176.2,8228.2,4254.52]
    runtime256 = [61970.8,32280.7,16333,8405.12]

fig, ax = plt.subplots()
ax.set_xscale('log', basex = 2)
ax.set_yscale('log', basey = 2)
ax.set_xticks([1, 2, 4, 8])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.plot(processes, runtime8, '-o', label='k = 8', color=colors[0])
ax.plot(processes, runtime16, '-o', label='k = 16', color=colors[1])
ax.plot(processes, runtime32, '-o', label='k = 32', color=colors[2])
ax.plot(processes, runtime64, '-o', label='k = 64', color=colors[3])
ax.plot(processes, runtime128, '-o', label='k = 128', color=colors[4])
ax.plot(processes, runtime256, '-o', label='k = 256', color=colors[5])

ax.legend().remove()
plt.ylabel("Parallel Runtime (milliseconds)")
plt.xlabel("No. of threads")
plt.title("Runtime vs. #threads for different walk length (ND)")
plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/FinalProject/Output/Runtime_ND.png', dpi = 500)

file = 4

if file == 1:
    speedup8 = [1,1.836852511,3.415735294,5.302968037]
    speedup16 = [1,1.84067086,3.49522293,4.787350055]
    speedup32 = [1,1.85960409,3.605482919,4.821545403]
    speedup64 = [1,1.835875332,3.568421053,6.496284709]
    speedup128 = [1,1.853567293,3.632832531,7.046325101]
    speedup256 = [1,1.84909614,3.595935934,7.052029915]
if file == 2:
    speedup8 = [1,1.959000217,3.871124674,7.596875291]
    speedup16 = [1,1.973896777,3.898513655,7.657939719]
    speedup32 = [1,1.97867609,3.898659112,7.608037435]
    speedup64 = [1,1.976451325,3.91251634,7.551240816]
    speedup128 = [1,1.972978702,3.897139608,7.529726119]
    speedup256 = [1,1.967591513,3.87887052,7.509064889]
if file == 3:
    speedup8 = [1,1.975483448,3.905677281,7.705116984]
    speedup16 = [1,1.986499373,3.881445904,7.613050861]
    speedup32 = [1,1.960465703,3.872425291,7.53477696]
    speedup64 = [1,1.951954965,3.862932368,7.502598419]
    speedup128 = [1,1.938474194,3.871476398,7.513756643]
    speedup256 = [1,1.981670803,3.871438098,7.480099149]
if file == 4:
    speedup8 = [1,1.923662175,3.758784057,7.382928202]
    speedup16 = [1,1.938901948,3.781675762,7.469103894]
    speedup32 = [1,1.924415822,3.771244133,7.366580805]
    speedup64 = [1,1.92242775,3.775208908,7.352891428]
    speedup128 = [1,1.935763653,3.805607545,7.360007709]
    speedup256 = [1,1.919747713,3.794208045,7.372982182]

fig, ax = plt.subplots()
ax.set_xscale('log', basex = 2)
ax.set_yscale('log', basey = 2)
ax.set_xticks([1, 2, 4, 8])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.plot(processes, speedup8, '-o', label='k = 8', color=colors[0])
ax.plot(processes, speedup16, '-o', label='k = 16', color=colors[1])
ax.plot(processes, speedup32, '-o', label='k = 32', color=colors[2])
ax.plot(processes, speedup64, '-o', label='k = 64', color=colors[3])
ax.plot(processes, speedup128, '-o', label='k = 128', color=colors[4])
ax.plot(processes, speedup256, '-o', label='k = 256', color=colors[5])

ax.legend().remove()
plt.ylabel("Speedup")
plt.xlabel("No. of threads")
plt.title("Speedup vs. #threads for different walk length (ND)")
plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/FinalProject/Output/Speedup_ND.png', dpi = 500)

file = 4

if file == 1:
    efficiency8 = [100,91.84262554,85.39338235,66.28710046]
    efficiency16 = [100,92.03354298,87.38057325,59.84187568]
    efficiency32 = [100,92.98020448,90.13707296,60.26931754]
    efficiency64 = [100,91.79376658,89.21052632,81.20355886]
    efficiency128 = [100,92.67836466,90.82081328,88.07906376]
    efficiency256 = [100,92.454807,89.89839834,88.15037393]
if file == 2:
    efficiency8 = [100,97.95001087,96.77811686,94.96094114]
    efficiency16 = [100,98.69483884,97.46284137,95.72424649]
    efficiency32 = [100,98.93380449,97.4664778,95.10046793]
    efficiency64 = [100,98.82256626,97.8129085,94.3905102]
    efficiency128 = [100,98.64893512,97.42849021,94.12157649]
    efficiency256 = [100,98.37957566,96.97176301,93.86331111]
if file == 3:
    efficiency8 = [100,98.77417239,97.64193202,96.3139623]
    efficiency16 = [100,99.32496863,97.0361476,95.16313576]
    efficiency32 = [100,98.02328516,96.81063226,94.184712]
    efficiency64 = [100,97.59774826,96.5733092,93.78248023]
    efficiency128 = [100,96.9237097,96.78690996,93.92195803]
    efficiency256 = [100,99.08354017,96.78595246,93.50123937]
if file == 4:
    efficiency8 = [100,96.18310873,93.96960142,92.28660253]
    efficiency16 = [100,96.9450974,94.54189405,93.36379867]
    efficiency32 = [100,96.22079111,94.28110331,92.08226006]
    efficiency64 = [100,96.12138752,94.38022271,91.91114285]
    efficiency128 = [100,96.78818264,95.14018862,92.00009637]
    efficiency256 = [100,95.98738565,94.85520113,92.16227728]
    
fig, ax = plt.subplots()
ax.set_xscale('log', basex = 2)
#ax.set_yscale('log', basey = 2)
ax.set_xticks([1, 2, 4, 8])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
#ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.plot(processes, efficiency8, '-o', label='k = 8', color=colors[0])
ax.plot(processes, efficiency16, '-o', label='k = 16', color=colors[1])
ax.plot(processes, efficiency32, '-o', label='k = 32', color=colors[2])
ax.plot(processes, efficiency64, '-o', label='k = 64', color=colors[3])
ax.plot(processes, efficiency128, '-o', label='k = 128', color=colors[4])
ax.plot(processes, efficiency256, '-o', label='k = 256', color=colors[5])

ax.legend().remove()
plt.ylabel("Efficiency (%)")
plt.xlabel("No. of threads")
plt.title("Efficiency vs. #threads for different walk length (ND)")
plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/FinalProject/Output/Efficiency_ND.png', dpi = 500)


arr = [100, 100, 100, 100]
fig, ax = plt.subplots()
ax.plot(processes, arr, label='k = 8', color=colors[0])
ax.plot(processes, arr, label='k = 16', color=colors[1])
ax.plot(processes, arr, label='k = 32', color=colors[2])
ax.plot(processes, arr, label='k = 64', color=colors[3])
ax.plot(processes, arr, label='k = 128', color=colors[4])
ax.plot(processes, arr, label='k = 256', color=colors[5])

plt.legend(loc="lower left", ncol=3, framealpha = 1.0)
plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/FinalProject/Output/Legend.png', dpi = 500)