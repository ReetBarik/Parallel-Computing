# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:19:09 2020

@author: reetb
"""

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np

# 1 for Naive, 2 for My, 3 for Library
processes = [1, 2, 4, 8, 16, 32]
choice = 2
number = 11
cmap = plt.get_cmap('gnuplot')
colors = [cmap(i) for i in np.linspace(0, 1, number)]

if choice == 1:
    runtime1k = [5,177,20526,51224,51333,60763]
    runtime2k = [18,173,30513,51156,51323,61121]
    runtime4k = [19,199,30598,50983,51437,61215]
    runtime8k = [38,202,30624,51039,51394,61190]
    runtime16k = [74,213,30500,51283,51411,61144]
    runtime32k = [149,289,30709,51094,51369,61064]
    runtime64k = [305,405,30631,51237,51314,61165]
    runtime128k = [594,512,30787,51190,51387,61172]
    runtime256k = [1189,807,30823,51257,51316,61095]
    runtime512k = [2380,1448,31075,51318,51545,61181]
    runtime1m = [4785,2605,31617,51489,51690,61161]
    
if choice == 2:
    runtime1k = [5,47,64,86,149,157]
    runtime2k = [11,45,56,83,151,174]
    runtime4k = [19,51,55,82,147,151]
    runtime8k = [38,57,57,88,131,158]
    runtime16k = [75,80,76,66,116,148]
    runtime32k = [149,118,112,111,84,154]
    runtime64k = [298,193,119,115,113,93]
    runtime128k = [596,341,209,192,181,176]
    runtime256k = [1191,629,442,243,220,198]
    runtime512k = [2386,1228,648,374,255,228]
    runtime1m = [4788,2448,1991,773,633,436]
    
if choice == 3:
    runtime1k = [5,42,98,204,10523,11378]
    runtime2k = [10,32,113,183,10564,11454]
    runtime4k = [19,52,81,206,10587,11437]
    runtime8k = [37,51,132,152,10777,11432]
    runtime16k = [72,67,160,158,10669,11353]
    runtime32k = [148,105,190,260,10631,11421]
    runtime64k = [295,170,130,208,10645,11413]
    runtime128k = [594,341,324,264,10731,11456]
    runtime256k = [1191,625,440,321,10742,11443]
    runtime512k = [2380,1226,689,503,10839,11567]
    runtime1m = [4788,2467,1402,906,10880,11440]
    
fig, ax = plt.subplots()
ax.set_xscale('log', basex = 2)
ax.set_yscale('log', basey = 2)
ax.set_xticks([1, 2, 4, 8, 16, 32])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.plot(processes, runtime1k, label='n = 1K', color=colors[0])
ax.plot(processes, runtime2k, label='n = 2K', color=colors[1])
ax.plot(processes, runtime4k, label='n = 4K', color=colors[2])
ax.plot(processes, runtime8k, label='n = 8K', color=colors[3])
ax.plot(processes, runtime16k, label='n = 16K', color=colors[4])
ax.plot(processes, runtime32k, label='n = 32K', color=colors[5])
ax.plot(processes, runtime64k, label='n = 64K', color=colors[6])
ax.plot(processes, runtime128k, label='n = 128K', color=colors[7])
ax.plot(processes, runtime256k, label='n = 256K', color=colors[8])
ax.plot(processes, runtime512k, label='n = 512K', color=colors[9])
ax.plot(processes, runtime1m, label='n = 1M', color=colors[10])

ax.legend().remove()
plt.ylabel("Parallel Runtime")
plt.xlabel("No. of processes")
plt.title("Runtime vs. #proceses for different input size")
if choice == 1:  
    plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment3/RuntimeNaive.png', dpi = 500)
if choice == 2:  
    plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment3/RuntimeMy.png', dpi = 500)
if choice == 3:  
    plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment3/RuntimeLibrary.png', dpi = 500)
    
if choice == 1:
    speedup1k = [1,0.028248588,0.000243593,0.000097610,0.000097403,0.000082287]
    speedup2k = [1,0.104046243,0.000589912,0.000351865,0.00035072,0.000294498]
    speedup4k = [1,0.095477387,0.000620956,0.000372673,0.000369384,0.000310381]
    speedup8k = [1,0.188118812,0.001240857,0.000744529,0.000739386,0.000621017]
    speedup16k = [1,0.34741784,0.00242623,0.001442973,0.001439381,0.001210258]
    speedup32k = [1,0.515570934,0.004851998,0.002916194,0.002900582,0.002440063]
    speedup64k = [1,0.75308642,0.009957233,0.005952729,0.005943797,0.004986512]
    speedup128k = [1,1.16015625,0.019293858,0.011603829,0.011559344,0.009710325]
    speedup256k = [1,1.473358116,0.03857509,0.023196832,0.023170161,0.019461494]
    speedup512k = [1,1.643646409,0.076588898,0.046377489,0.046173247,0.038900966]
    speedup1m = [1,1.836852207,0.151342632,0.092932471,0.092571097,0.078236131]
    
if choice == 2:
    speedup1k = [1,0.106382979,0.078125,0.058139535,0.033557047,0.031847134]
    speedup2k = [1,0.244444444,0.196428571,0.13253012,0.072847682,0.063218391]
    speedup4k = [1,0.37254902,0.345454545,0.231707317,0.129251701,0.125827815]
    speedup8k = [1,0.666666667,0.666666667,0.431818182,0.290076336,0.240506329]
    speedup16k = [1,0.9375,0.986842105,1.136363636,0.646551724,0.506756757]
    speedup32k = [1,1.262711864,1.330357143,1.342342342,1.773809524,0.967532468]
    speedup64k = [1,1.544041451,2.504201681,2.591304348,2.637168142,3.204301075]
    speedup128k = [1,1.747800587,2.851674641,3.104166667,3.29281768,3.386363636]
    speedup256k = [1,1.893481717,2.694570136,4.901234568,5.413636364,6.015151515]
    speedup512k = [1,1.942996743,3.682098765,6.379679144,9.356862745,10.46491228]
    speedup1m = [1,1.955882353,2.404821698,6.194049159,7.563981043,10.98165138]
    
if choice == 3:
    speedup1k = [1,0.119047619,0.051020408,0.024509804,0.00047515,0.000439445]
    speedup2k = [1,0.3125,0.088495575,0.054644809,0.000946611,0.000873057]
    speedup4k = [1,0.365384615,0.234567901,0.09223301,0.001794654,0.001661275]
    speedup8k = [1,0.725490196,0.28030303,0.243421053,0.003433237,0.003236529]
    speedup16k = [1,1.074626866,0.45,0.455696203,0.006748524,0.006341936]
    speedup32k = [1,1.40952381,0.778947368,0.569230769,0.01392155,0.012958585]
    speedup64k = [1,1.735294118,2.269230769,1.418269231,0.027712541,0.025847718]
    speedup128k = [1,1.741935484,1.833333333,2.25,0.055353648,0.051850559]
    speedup256k = [1,1.9056,2.706818182,3.710280374,0.110873208,0.104081098]
    speedup512k = [1,1.941272431,3.454281567,4.731610338,0.219577452,0.205757759]
    speedup1m = [1,1.940818808,3.415121255,5.284768212,0.440073529,0.418531469]
    
fig, ax = plt.subplots()
ax.set_xscale('log', basex = 2)
ax.set_yscale('log', basey = 2)
ax.set_xticks([1, 2, 4, 8, 16, 32])
ax.set_yticks([0.015, 0.031, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.plot(processes, speedup1k, label='n = 1K', color=colors[0])
ax.plot(processes, speedup2k, label='n = 2K', color=colors[1])
ax.plot(processes, speedup4k, label='n = 4K', color=colors[2])
ax.plot(processes, speedup8k, label='n = 8K', color=colors[3])
ax.plot(processes, speedup16k, label='n = 16K', color=colors[4])
ax.plot(processes, speedup32k, label='n = 32K', color=colors[5])
ax.plot(processes, speedup64k, label='n = 64K', color=colors[6])
ax.plot(processes, speedup128k, label='n = 128K', color=colors[7])
ax.plot(processes, speedup256k, label='n = 256K', color=colors[8])
ax.plot(processes, speedup512k, label='n = 512K', color=colors[9])
ax.plot(processes, speedup1m, label='n = 1M', color=colors[10])

ax.legend().remove()
plt.ylabel("Speedup")
plt.xlabel("No. of processes")
plt.title("Speedup vs. #proceses for different input size")
if choice == 1:  
    plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment3/SpeedupNaive.png', dpi = 500)
if choice == 2:  
    plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment3/SpeedupMy.png', dpi = 500)
if choice == 3:  
    plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment3/SpeedupLibrary.png', dpi = 500)
    
if choice == 1:
    efficiency1k = [100,1.412429379,0.006089837,0.001220131,0.00060877,0.000257147]
    efficiency2k = [100,5.202312139,0.014747812,0.004398311,0.002192,0.000920306]
    efficiency4k = [100,4.773869347,0.01552389,0.004658416,0.002308649,0.000969942]
    efficiency8k = [100,9.405940594,0.031021421,0.009306609,0.004621162,0.001940677]
    efficiency16k = [100,17.37089202,0.060655738,0.018037166,0.008996129,0.003782055]
    efficiency32k = [100,25.77854671,0.121299945,0.036452421,0.018128638,0.007625197]
    efficiency64k = [100,37.65432099,0.248930822,0.074409118,0.037148731,0.01558285]
    efficiency128k = [100,58.0078125,0.482346445,0.145047861,0.072245899,0.030344766]
    efficiency256k = [100,73.66790582,0.964377251,0.289960396,0.144813508,0.06081717]
    efficiency512k = [100,82.18232044,1.914722446,0.579718617,0.288582792,0.121565519]
    efficiency1m = [100,91.84261036,3.783565803,1.161655888,0.578569356,0.244487909]
    
if choice == 2:
    efficiency1k = [100,5.319148936,1.953125,0.726744186,0.209731544,0.099522293]
    efficiency2k = [100,12.22222222,4.910714286,1.656626506,0.455298013,0.197557471]
    efficiency4k = [100,18.62745098,8.636363636,2.896341463,0.807823129,0.393211921]
    efficiency8k = [100,33.33333333,16.66666667,5.397727273,1.812977099,0.751582278]
    efficiency16k = [100,46.875,24.67105263,14.20454545,4.040948276,1.583614865]
    efficiency32k = [100,63.13559322,33.25892857,16.77927928,11.08630952,3.023538961]
    efficiency64k = [100,77.20207254,62.60504202,32.39130435,16.48230088,10.01344086]
    efficiency128k = [100,87.39002933,71.29186603,38.80208333,20.5801105,10.58238636]
    efficiency256k = [100,94.67408585,67.36425339,61.2654321,33.83522727,18.79734848]
    efficiency512k = [100,97.14983713,92.05246914,79.7459893,58.48039216,32.70285088]
    efficiency1m = [100,97.79411765,60.12054244,77.42561449,47.27488152,34.31766055]
    
if choice == 3:
    efficiency1k = [100,5.952380952,1.275510204,0.306372549,0.002969685,0.001373264]
    efficiency2k = [100,15.625,2.212389381,0.683060109,0.011832639,0.002728305]
    efficiency4k = [100,18.26923077,5.864197531,1.152912621,0.022433173,0.005191484]
    efficiency8k = [100,36.2745098,7.007575758,3.042763158,0.042915468,0.010114153]
    efficiency16k = [100,53.73134328,11.25,5.696202532,0.084356547,0.01981855]
    efficiency32k = [100,70.47619048,19.47368421,7.115384615,0.174019377,0.040495578]
    efficiency64k = [100,86.76470588,56.73076923,17.72836538,0.346406764,0.080774117]
    efficiency128k = [100,87.09677419,45.83333333,28.125,0.691920604,0.162032996]
    efficiency256k = [100,95.28,67.67045455,46.37850467,1.3859151,0.32525343]
    efficiency512k = [100,97.06362153,86.35703919,59.14512922,2.744718147,0.642992997]
    efficiency1m = [100,97.04094041,85.37803138,66.05960265,5.500919118,1.307910839]
    
fig, ax = plt.subplots()
ax.set_xscale('log', basex = 2)
ax.set_xticks([1, 2, 4, 8, 16, 32])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter()) 
ax.plot(processes, efficiency1k, label='n = 1K', color=colors[0])
ax.plot(processes, efficiency2k, label='n = 2K', color=colors[1])
ax.plot(processes, efficiency4k, label='n = 4K', color=colors[2])
ax.plot(processes, efficiency8k, label='n = 8K', color=colors[3])
ax.plot(processes, efficiency16k, label='n = 16K', color=colors[4])
ax.plot(processes, efficiency32k, label='n = 32K', color=colors[5])
ax.plot(processes, efficiency64k, label='n = 64K', color=colors[6])
ax.plot(processes, efficiency128k, label='n = 128K', color=colors[7])
ax.plot(processes, efficiency256k, label='n = 256K', color=colors[8])
ax.plot(processes, efficiency512k, label='n = 512K', color=colors[9])
ax.plot(processes, efficiency1m, label='n = 1M', color=colors[10])

ax.legend().remove()
plt.ylabel("Efficiency")
plt.xlabel("No. of processes")
plt.title("Efficiency vs. #proceses for different input size")
if choice == 1:  
    plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment3/EfficiencyNaive.png', dpi = 500)
if choice == 2:  
    plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment3/EfficiencyMy.png', dpi = 500)
if choice == 3:  
    plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment3/EfficiencyLibrary.png', dpi = 500)

arr = [100, 100, 100, 100, 100, 100]
fig, ax = plt.subplots()
ax.plot(processes, arr, label='n = 1K', color=colors[0])
ax.plot(processes, arr, label='n = 2K', color=colors[1])
ax.plot(processes, arr, label='n = 4K', color=colors[2])
ax.plot(processes, arr, label='n = 8K', color=colors[3])
ax.plot(processes, arr, label='n = 16K', color=colors[4])
ax.plot(processes, arr, label='n = 32K', color=colors[5])
ax.plot(processes, arr, label='n = 64K', color=colors[6])
ax.plot(processes, arr, label='n = 128K', color=colors[7])
ax.plot(processes, arr, label='n = 256K', color=colors[8])
ax.plot(processes, arr, label='n = 512K', color=colors[9])
ax.plot(processes, arr, label='n = 1M', color=colors[10])

plt.legend(loc="lower left", ncol=4, framealpha = 1.0)
plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment3/Legend.png', dpi = 500)
    
    
