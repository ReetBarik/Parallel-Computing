# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:23:34 2020

@author: reetb
"""

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np


speedup64 = [1, 1.885262939, 3.444085817, 5.271723336, 0.16268766, 0.086834144]
speedup128 = [1, 1.903508772, 3.643821023, 6.677854221, 0.567282176, 0.328047572]
speedup256 = [1, 1.847583055, 3.711887315, 7.15334525, 1.969493504, 1.288043553]
speedup512 = [1, 1.858730361, 3.696130045, 7.29228927, 5.597090822, 4.509233735]


Eff64 = [100, 94.26314695, 86.10214543, 65.8965417, 1.016797905, 0.2713567]
Eff128 = [100	, 95.1754386, 91.09552557, 83.47317776, 3.5455136, 1.025148662]
Eff256 = [100	, 92.37915273, 92.79718287, 89.41681563, 12.3093344, 4.025136104]
Eff512 = [100	, 92.93651807, 92.40325113, 91.15361587, 34.98181764, 14.09135542]


processes = [1, 2, 4, 8, 16, 32]


fig, ax = plt.subplots()
ax.set_xscale('log', basex = 2)
ax.set_yscale('log', basey = 2)
ax.set_xticks([1, 2, 4, 8, 16, 32])
ax.set_yticks([0.125, 0.25, 0.5, 1, 2, 4, 8])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.plot(processes, speedup64, label='n = 64')
ax.plot(processes, speedup128, label='n = 128')
ax.plot(processes, speedup256, label='n = 256')
ax.plot(processes, speedup512, label='n = 512')

ax.legend()
plt.ylabel("Speedup")
plt.xlabel("No. of processes")
plt.title("Speedup vs. #proceses for different input size")
          
plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment2/Speedup.png', dpi = 500)


fig, ax = plt.subplots()
ax.set_xscale('log', basex = 2)
ax.set_xticks([1, 2, 4, 8, 16, 32])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.plot(processes, Eff64, label='n = 64')
ax.plot(processes, Eff128, label='n = 128')
ax.plot(processes, Eff256, label='n = 256')
ax.plot(processes, Eff512, label='n = 512')

ax.legend()
plt.ylabel("Efficiency")
plt.xlabel("No. of processes")
plt.title("Efficiency vs. #proceses for different input size")
          
plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment2/Efficiency.png', dpi = 500)




commTime = (334, 609, 1276, 1490, 122251, 214376)
compTime = (71493, 37125, 18436, 9266, 4365, 4577)


ind = np.arange(6)

width = 0.35

p1 = plt.bar(ind, commTime, width)
p2 = plt.bar(ind, compTime, width, bottom=commTime)

plt.ylabel('Total Runtime (microseconds)')
plt.title('Runtime breakdown for diff #processes (n = 128)')
plt.xticks(ind, ('1', '2', '4', '8', '16', '32'))
plt.legend((p1[0], p2[0]), ('Communication', 'Computation'))
plt.savefig('C:/Users/reetb/Desktop/Parallel-Computing/Assignment2/Breakup.png', dpi = 500)





























