#
# Code used for analysing ITU constellation data 
# by etwright1 (E. Wright), 2023
#


import numpy as np
import matplotlib.pylab as plt
import datetime as dt
import matplotlib.dates as mdates

data = np.genfromtxt('ITU constellation filings data for plot.csv', dtype=None, delimiter=',', encoding='utf-8-sig', skip_header=1)

individual = []
cumulative = []
cumu_no = []
dates = []
largedates = []

for line in data:
    y = line[0]
    z = dt.datetime.strptime(y,'%d-%m-%y').date()
    dates = np.append(dates, z)
    if int(line[1]) > 10000:
        individual = np.append(individual, line[1])
        largedates = np.append(largedates, z)
    cumulative = np.append(cumulative, line[2])
    cumu_no = np.append(cumu_no, line[3])

fontsize = 6
plt.figure(figsize=(4, 3), dpi=300)
plt.rc('font', size=fontsize)  
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.plot(dates, cumu_no/1000, label= 'Cumulative satellites filed excluding Cinnamon', color='#bc5090', linestyle='dashed',zorder=1)
plt.plot(dates, cumulative/1000, label= 'Cumulative satellites filed including Cinnamon', color='#003f5c', zorder=2)
plt.scatter(largedates, individual/1000, label= 'No. of satellites in filings > 10,000 satellites', color='#ff6361', marker='+', s=30, zorder=3)
plt.xlabel("Year", color='#000000')
plt.yticks(np.arange(0, 1201, 200))

end_date = '01-01-23'
end_date = dt.datetime.strptime(end_date,'%d-%m-%y').date()
dates = np.append(dates, end_date)

plt.xlim((min(dates),max(dates)))
plt.ylim((0,1100))
plt.gcf().autofmt_xdate()
plt.ylabel('Number of satellites / thousands', color='#000000')
plt.legend(loc=2)
plt.grid(b=True, alpha=0.25)
plt.tight_layout()
plt.savefig('plot.svg')
plt.show()
