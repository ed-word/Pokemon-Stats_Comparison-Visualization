import pandas as pd 
from collections import defaultdict
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
import numpy as np
plt.style.use('ggplot')

new_df = pd.read_csv("Pokemon.csv")
#print(new_df.head())


###############################################################################################

Pokemon1_name = 'Mewtwo'
Pokemon2_name = 'Articuno'

Pokemon1 = new_df.loc[ new_df['Name']==Pokemon1_name ]
Pokemon2 = new_df.loc[ new_df['Name']==Pokemon2_name ]

labels = 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'HP', 'Speed'

P1_data=[]
for i in labels:
	P1_data.append( int(Pokemon1[i]) )

P2_data=[]
for i in labels:
	P2_data.append( int(Pokemon2[i]) )



##########################Pie Chart#################################################################
index = P1_data.index( max(P1_data) )

explode = [0, 0, 0, 0, 0]
explode.insert(index,0.1)


fig1, ax1 = plt.subplots()
ax1.pie(P1_data, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
plt.title(Pokemon1_name+" Stats")
plt.show()



index = P2_data.index( max(P2_data) )

explode = [0, 0, 0, 0, 0]
explode.insert(index,0.1)


fig2, ax2 = plt.subplots()
ax2.pie(P2_data, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.axis('equal') 
plt.title(Pokemon2_name+" Stats")
plt.show()


#########################################Radar Chart#######################################################
# A radar chart example: http://datascience.stackexchange.com/questions/6084/how-do-i-create-a-complex-radar-chart
def _scale_data(data, ranges):
    (x1, x2), d = ranges[0], data[0]
    return [(d - y1) / (y2 - y1) * (x2 - x1) + x1 for d, (y1, y2) in zip(data, ranges)]

class RaderChart():
    def __init__(self, fig, variables, ranges, n_ordinate_levels = 6):
        angles = np.arange(0, 360, 360./len(variables))

        axes = [fig.add_axes([0.1,0.1,0.8,0.8],polar = True, label = "axes{}".format(i)) for i in range(len(variables))]
        _, text = axes[0].set_thetagrids(angles, labels = variables)
        
        for txt, angle in zip(text, angles):
            txt.set_rotation(angle - 90)
        
        for ax in axes[1:]:
            ax.patch.set_visible(False)
            ax.xaxis.set_visible(False)
            ax.grid('off')
        
        for i, ax in enumerate(axes):
            grid = np.linspace(*ranges[i], num = n_ordinate_levels)
            grid_label = ['']+[str(int(x)) for x in grid[1:]]
            ax.set_rgrids(grid, labels = grid_label, angle = angles[i])
            ax.set_ylim(*ranges[i])
        
        self.angle = np.deg2rad(np.r_[angles, angles[0]])
        self.ranges = ranges
        self.ax = axes[0]

    def plot(self, data, *args, **kw):
        sdata = _scale_data(data, self.ranges)
        self.ax.plot(self.angle, np.r_[sdata, sdata[0]], *args, **kw)

    def fill(self, data, *args, **kw):
        sdata = _scale_data(data, self.ranges)
        self.ax.fill(self.angle, np.r_[sdata, sdata[0]], *args, **kw)

    def legend(self, *args, **kw):
        self.ax.legend(*args, **kw)



max_val=[]
for i in range(len(P1_data)):
    max_val.append( max(P1_data[i],P2_data[i]) )

ranges = [[2**-20, mv] for mv in max_val]



fig = plt.figure(figsize=(10, 10))
radar = RaderChart(fig, labels, ranges)

radar.plot(P1_data, color = 'r', label = Pokemon1_name)
radar.fill(P1_data, alpha = 0.1, color = 'r')
radar.legend(loc = 1, fontsize = 'small')

radar.plot(P2_data, color = 'b', label = Pokemon2_name)
radar.fill(P2_data, alpha = 0.1, color = 'b')
radar.legend(loc = 1, fontsize = 'small')

plt.title(Pokemon1_name+" vs "+Pokemon2_name)
plt.show()

##############################Type comparison Main Bar Graph######################################

ind = np.arange(6)  		# the x locations for the groups
width = 0.25      			# the width of the bars

fig, ax = plt.subplots()

ax.bar(ind, P1_data, width, color='r') 
ax.bar(ind + width, P2_data, width, color='b') 

ax.set_xticks(ind + width / 2)
ax.set_xticklabels(labels)
plt.title(Pokemon1_name+" vs "+Pokemon2_name)
plt.show()
