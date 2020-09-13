import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')


messageSize = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152]

blockingSend = [19968,10,8.1,8.1,3,4.1,11.2,10.2,10.9,11.9,12.3,18,16,21.5,34.7,40.7,656.3,803.3,1485.3,3418.2,7024.4,14094.6]

blockingRecv = [20212.7,27.7,3.4,53.9,1,8.5,1,13.8,5.6,38,9.5,53.6,80.4,56.3,162.9,231.7,740.8,1276,2390.2,4617.9,9077.8,17993.9]

nonBlockingSend = [19986.4,9.6,6.7,9.4,3.8,7.6,16.1,10.3,10.7,9.1,16.9,14.4,16.6,18.2,36,32.6,639.3,748,1389.8,3180.9,7757.2,14348.6]

nonBlockingRecv = [20212.8,25,2.6,61.1,1.8,23.3,1.8,17.7,15.5,51.1,9.5,48.3,74,56.8,168.3,202.1,731.5,1274,2395,4623.9,9077.7,17996.1]

magnifiedBlockingRecv = [740.8,1276,2390.2,4617.9,9077.8,17993.9]

magnifiedNonBlockingRecv = [731.5,1274,2395,4623.9,9077.7,17996.1]

fig, ax = plt.subplots()
ax.plot(messageSize, blockingSend, label='Send')
ax.plot(messageSize, blockingRecv, label='Recv' )
ax.set_xscale('log')
ax.set_xticks([1,64,2048,131072,2097152])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.legend()
plt.ylabel("Time (us)")
plt.xlabel("Message Size (bytes)")
plt.title("Comm time vs Message Size (Blocking)")
plt.savefig('BlockingPlot.png', dpi = 500)


fig, ax = plt.subplots()
ax.plot(messageSize, nonBlockingSend, label='Send')
ax.plot(messageSize, nonBlockingRecv, label='Recv' )
ax.set_xscale('log')
ax.set_xticks([1,64,2048,131072,2097152])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.legend()
plt.ylabel("Time (us)")
plt.xlabel("Message Size (bytes)")
plt.title("Comm time vs Message Size (Non-Blocking)")
plt.savefig('NonBlockingPlot.png', dpi = 500)


fig, ax = plt.subplots()
ax.plot([65536,131072,262144,524288,1048576,2097152], magnifiedBlockingRecv, label='Recv')
ax.set_xticks([500000,1000000,1500000,2000000])
ax.legend()
plt.ylabel("Time (us)")
plt.xlabel("Message Size (bytes)")
plt.title("After breaking even (Blocking)")
plt.savefig('MagBlockingPlot.png', dpi = 500)


fig, ax = plt.subplots()
ax.plot([65536,131072,262144,524288,1048576,2097152], magnifiedNonBlockingRecv, label='Recv')
ax.set_xticks([500000,1000000,1500000,2000000])
ax.legend()
plt.ylabel("Time (us)")
plt.xlabel("Message Size (bytes)")
plt.title("After breaking even (Non-Blocking)")
plt.savefig('MagNonBlockingPlot.png', dpi = 500)
















