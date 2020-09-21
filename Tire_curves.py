import pandas as pa
import matplotlib.pyplot as plt
import seaborn as sns

to_be_compared_list = ('datafile1.dat', 'datafile2.dat')
# add the data files of interest in the folder and update the link(s) in the list


def slip_angles(link):
    run = pa.read_csv(f'{link}', sep='\t', header=1)
    n_column = []

    for i in range(run.columns.size):
        temp = run.columns[i] + ' (' + run.iloc[0, i] + ')'
        n_column.append(temp)

    run.columns = n_column
    reformatted = run.drop([0])
    reformatted = reformatted[:7300]
    reformatted = reformatted.astype(float)

    sns.set()
    plt.plot()
    plt.plot(reformatted['SA (deg)'], reformatted['FY (lb)'])


for file in to_be_compared_list:
    slip_angles(f'{file}')

plt.ylabel('Lateral Load (lb)')
plt.xlabel('Slip Angles (deg)')
plt.title('Random Tire data Curves')
plt.axis([-13, 13, -650, 650])

plt.savefig('tire_data.png', dpi=400)
plt.show()

quit()
