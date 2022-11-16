import matplotlib.pyplot as plt
import numpy as np
place=['1st','2nd','3rd']
pcm_percentage=[80,90,100]
pcb_percenatge=[90,100,80]
comm_percentage=[100,90,80]
x=np.arange(len(place))
plt.bar(x,pcm_percentage, label='PCM', width=0.25, color='black')
plt.bar(x+.25,pcb_percenatge, label='PCB', width=0.25, color='magenta')
plt.bar(x+.50,comm_percentage, label='Commerce', width=0.25, color='yellow')
plt.xticks(x,place)
plt.xlabel('Position')
plt.ylabel('Percentage')
plt.title('Result Analysis Bar Graph')
plt.legend()
plt.show()
