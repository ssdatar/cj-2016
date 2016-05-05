from os.path import join
import matplotlib.pyplot as plt
import pandas as pd

folder = join('matplotlibsampler', 'data', 'schools')
frpm_file = join(folder, 'frpm-2014.csv')
sat_file = join(folder, 'sat-2014.csv')

frpm_df = pd.read_csv(frpm_file, na_values=['*'])
sat_df = pd.read_csv(sat_file, na_values=['*'])

sat_df = sat_df[sat_df['number_of_test_takers'] >= 20]

combined = pd.merge(left=sat_df, right=frpm_df, on='cds')

fig, ax = plt.subplots()
ax.set_xlabel('Percentage of scores >= 1500')
ax.set_ylabel('Number of schools')
ax.set_title('Average SAT scores per school, 2014')

rich = combined[combined['adjusted_pct_eligible_frpm_k12'] < 0.5]
poor = combined[combined['adjusted_pct_eligible_frpm_k12'] >= 0.5]
datalist = [rich['percent_scores_gte_1500'], poor['percent_scores_gte_1500']]

ax.hist(datalist, bins=25, stacked=True, color=['darkred', 'gray'])
ax.set_xlabel('Percentage of scores >= 1500')
ax.set_ylabel('Number of schools');
ax.legend(['< 50% kids get free meals', '>= 50% kids get free meals'])

plt.show()
plt.savefig('stacked.png')

