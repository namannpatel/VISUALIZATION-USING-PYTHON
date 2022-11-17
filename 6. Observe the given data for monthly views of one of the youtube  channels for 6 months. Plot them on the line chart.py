import matplotlib.pyplot as pp
mon =['January','February','March','April','May','June']
views = [2500,2100,1700,3500,3000,3800]
pp.plot(mon,views,label='Views''State',color='r',linestyle='dashed', linewidth=4, 
marker='o', markerfacecolor='k', markeredgecolor='b')
pp.title("Youtube Stats")
pp.xlabel("Months")
pp.ylabel("Views")
pp.legend()
pp.show()
