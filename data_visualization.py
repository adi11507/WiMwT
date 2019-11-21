import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns


def get_stats(datas):
    # maksimum, minimum, rozstep
    max_datas = np.max(datas)
    min_datas = np.min(datas)
    gaps = max_datas - min_datas
    # srednia, mediana, modalna
    mean_datas = np.mean(datas)
    median_datas = np.median(datas, axis=0)
    modes, counts = stats.mode(datas, axis=0)
    # skosnosc, kurioza, odchylenie
    skews = stats.skew(datas)
    kurt_datas = stats.kurtosis(datas)
    std_datas = np.std(datas)
    return max_datas, min_datas, gaps, mean_datas, median_datas, modes, counts, skews, kurt_datas, std_datas


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if height > 0:
            ax.annotate('{0:.4f}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
        else:
            ax.annotate('{0:.4f}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, -3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='top')


dataFileUrl = "dane.xlsx"
data = pd.read_excel(dataFileUrl, sheet_name='B2', usecols='A,B,C,D,E,F')

max_data, min_data, gap, mean_data, median_data, mode, count, skew, kurt_data, std_data = get_stats(data)

# maksimum wykres
labels = ['S1 - skroń', 'S1 - udo', 'S2 - skroń', 'S2 - udo', 'S3 - skroń', 'S3 - udo']
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x, max_data, width, label='Maksimum', color='skyblue')
ax.set_ylabel('Maksimum')
ax.set_title('Wartość maksymalna')
plt.ylim(0, 60)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
autolabel(rects1)

# minimum wykres
fig2, ax = plt.subplots()
rects2 = ax.bar(x, min_data, width, label='Minimum', color='skyblue')
ax.set_ylabel('Minimum')
ax.set_title('Wartość minimalna')
plt.ylim(0, 45)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
autolabel(rects2)

# rozstęp wykres
fig3, ax = plt.subplots()
rects3 = ax.bar(x, gap, width, label='Rozstęp', color='skyblue')
ax.set_ylabel('Rozstęp')
plt.ylim(0, 31)
ax.set_title('Wartości rozstępu')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
autolabel(rects3)

# średnia wykres
fig4, ax = plt.subplots()
rects4 = ax.bar(x, mean_data, width, label='Średnia', color='limegreen')
ax.set_ylabel('Wartość średnia')
ax.set_title('Średnia arytmetyczna')
plt.ylim(35, 39)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
autolabel(rects4)

# mediana wykres
fig5, ax = plt.subplots()
rects5 = ax.bar(x, median_data, width, label='Mediana', color='limegreen')
ax.set_ylabel('Mediana')
ax.set_title('Mediana')
plt.ylim(35, 39)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
autolabel(rects5)

# modalna wykres
fig6, ax = plt.subplots()
rects6 = ax.bar(x, mode[0], width, label='Modalna', color='limegreen')
ax.set_ylabel('Wartość modalna')
ax.set_title('Wartość modalna')
plt.ylim(32, 42)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
autolabel(rects6)

# skosnosc wykres
fig7, ax = plt.subplots()
colors = ['darkorange', 'darkorange', 'darkorange', 'skyblue', 'skyblue', 'skyblue']
rects7 = ax.bar(x, skew, width, label='Skośność', color=colors)
plt.axhline(0, label='zero', color='grey', zorder=1)
ax.set_ylabel('Skośność')
ax.set_title('Skośność')
plt.ylim(-0.1, 0.1)

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
autolabel(rects7)

# kurtoza wykres
fig8, ax = plt.subplots()
plt.axhline(0, label='zero', color='grey', zorder=1)
rects8 = ax.bar(x, kurt_data, width, label='Kurtoza', color='darkorange')
ax.set_ylabel('Kurtoza')
ax.set_title('Kurtoza')
plt.ylim(-1.5, 1.5)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
autolabel(rects8)

# odchylenie standardowe
fig9, ax = plt.subplots()

bar = plt.errorbar(x, mean_data, yerr=std_data, label='Odchylenie standardowe', linestyle='None', marker='^',
                   ecolor='red', elinewidth=1.5, capsize=5, capthick=2)
ax.set_ylabel('Odchylenie standardowe')
ax.set_title('Odchylenie standardowe')  
plt.ylim(36, 38)
ax.set_xticks(x)
ax.set_xticklabels(labels)
print(mean_data[0])
print(str(std_data[0]))
for i in range(0, 6):
    plt.text(x[i], mean_data[i], str('{0:.4f}'.format(std_data[i])), fontsize=9)

ax.legend()

fig10, ax = plt.subplots()
sns.set_style('whitegrid')
sns.distplot(data['Seria1_1'], kde=True, color='red', label='Seria 1 - Skroń')
sns.distplot(data['Seria1_2'], kde=True, color='skyblue', label='Seria 1 - Udo')
ax.set_xlabel('Temperatura ciała [°C]')
ax.set_ylabel('Częstotliwość')
ax.set_title('Rozkład prawdopodobieństwa - Seria 1')
plt.legend(prop={'size': 10}, title='Seria')

fig11, ax = plt.subplots()
sns.set_style('whitegrid')
sns.distplot(data['Seria2_1'], kde=True, color='red', bins=30, label='Seria 2 - Skroń')
sns.distplot(data['Seria_2_2'], kde=True, color='skyblue', bins=30, label='Seria 2 - Udo')
ax.set_xlabel('Temperatura ciała [°C]')
ax.set_ylabel('Częstotliwość')
ax.set_title('Rozkład prawdopodobieństwa - Seria 2')
plt.legend(prop={'size': 10}, title='Seria')

fig12, ax = plt.subplots()
sns.set_style('whitegrid')
sns.distplot(data['Seria_3_1'], kde=True, color='red', bins=30, label='Seria 3 - Skroń')
sns.distplot(data['Seria_3_2'], kde=True, color='skyblue', label='Seria 3 - Udo')
ax.set_ylabel('Częstotliwość')
ax.set_xlabel('Temperatura ciała [°C]')
ax.set_title('Rozkład prawdopodobieństwa - Seria 3')
plt.legend(prop={'size': 10}, title='Seria')

fig13, ax = plt.subplots()
l1 = sns.distplot(data['Seria1_2'], kde=True, color='skyblue', bins=30, label='Seria 1 - udo')
l2 = sns.distplot(data['Seria2_1'], kde=True, color='yellow', bins=30, label='Seria 2 - skroń')
l3 = sns.distplot(data['Seria_2_2'], kde=True, color='olive', bins=30, label='Seria 2 - udo')
l4 = sns.distplot(data['Seria_3_1'], kde=True, color='black', bins=30, label='Seria 3 - skroń')
l5 = sns.distplot(data['Seria_3_2'], kde=True, color='red', bins=30, label='Seria 3 - udo')
plt.legend(prop={'size': 10}, title='Seria')
plt.title('Rozkład prawdopodobieństwa')
plt.xlabel('Temperatura Ciała [°C]')
plt.ylabel('Częstotliwość')

plt.show()
