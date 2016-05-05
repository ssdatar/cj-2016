from os.path import join
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

folder = join('matplotlibsampler', 'data', 'congress')
the_file = join(folder, 'legislators-twitter.csv')

leg_df = pd.read_csv(the_file, na_values=['*'], parse_dates=['Since'])

fig, ax = plt.subplots()

ax.scatter(leg_df['Tweets'], leg_df['Favorites'])

ax.set_xlabel('Tweets')
ax.set_ylabel('Favorites')
ax.set_ylim(ymin=0)
ax.set_xlim(xmin=0)

plt.show()
plt.savefig('scatter.png')