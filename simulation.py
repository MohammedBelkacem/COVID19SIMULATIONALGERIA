global_population=40000000 #population globale
start_number=141 # nombre de personnes atteinte au départ
mortality_rate=4 # taux de mortalité
day=1 #intervalle
speed=1.5 #vitesse de propagation par jour
reached_population=int(global_population/3) # max population cible atteinte.
number=start_number#nombre de personnes atteinte dans le temps
mortality=mortality_rate*number/100
tab_mortality=[]
tab_number=[]
tab_day=[]
tab_mortality.append(mortality)
tab_number.append(number)
tab_day.append(day)
tot_mort=start_number/mortality_rate
while number<reached_population:
    day=day+1
    number=number*speed+number
    mortality=mortality_rate*number/100
    tab_mortality.append(mortality)
    tab_number.append(number)
    tab_day.append(day)
    number=number-mortality
    tot_mort=tot_mort+mortality

print("le PIC dans ",day," jours")
print("Nombre total de morts  ", int(tot_mort))

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = tab_day
women_means = tab_number
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects2 = ax.bar(x + width/2, women_means, width, label='Confirmés')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Evolution du nombre de personnes atteinte en Algérie')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects2)

fig.tight_layout()

plt.show()
######
labels = tab_day
men_means = tab_mortality
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Morts')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Evolution du nombre de morts en Algérie')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)

fig.tight_layout()

plt.show()
