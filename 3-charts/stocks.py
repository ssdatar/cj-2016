from os.path import join, basename
from glob import glob
import csv
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib.dates import date2num
from matplotlib.dates import MONDAY, MonthLocator, WeekdayLocator, DateFormatter

files = glob(join('../matplotlibsampler', 'data', 'stocks', '*.csv'))

master = {}

# every 3rd month
months = MonthLocator(range(1, 13), bymonthday=1, interval=3)
monthsFmt = DateFormatter("%b '%y")

for f in files:
    name = basename(f)[:-4] #Extract stock name, remove .csv extension

    if not master.get(name):
        master[name] = []

    with open(f, 'r') as csv_in:
        print('Currently on', name)
        
        datarows = list(csv.DictReader(csv_in))

        close_price = [d['Adj Close'] for d in datarows]
        # Convert the date string to a number
        dates = [dt.datetime.strptime(d['Date'], '%Y-%m-%d') for d in datarows]

        temp = [dates, close_price]
        master[name] = temp

fig, ax = plt.subplots()

for company in master:
    x = master[company][0]
    y = master[company][1]
    ax.plot_date(x, y, '-', label=company)

# Set x labels
ax.set_xticks(x)

# Format month ticks: http://matplotlib.org/examples/pylab_examples/date_demo2.html
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)
fig.autofmt_xdate()
   
# ax.set_xticks(x)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)
ax.grid(True)
plt.savefig('stocks.png')
plt.show()