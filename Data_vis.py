import pandas as pd 
from collections import defaultdict
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
import numpy as np
plt.style.use('ggplot')

df = pd.read_csv("Pokemon.csv")
#print(df.head())


new_df = df
new_df.drop( ['#'], 1, inplace=True )
new_df.drop( ['Type 2'], 1, inplace=True )
new_df.drop( ['Generation'], 1, inplace=True )
new_df.drop( ['Legendary'], 1, inplace=True )

#print(new_df.head())


##########################Colors############################################################
Colors = dict()
Colors['Normal'] = '#A8A77A'
Colors['Fire'] = '#EE8130'
Colors['Water'] = '#6390F0'
Colors['Electric'] = '#F7D02C'
Colors['Grass'] = '#7AC74C'
Colors['Ice'] = '#96D9D6'
Colors['Fighting'] = '#C22E28'
Colors['Poison'] = '#A33EA1'
Colors['Ground'] = '#E2BF65'
Colors['Flying'] = '#A98FF3'
Colors['Psychic'] = '#F95587'
Colors['Bug'] = '#A6B91A'
Colors['Rock'] = '#B6A136'
Colors['Ghost'] = '#735797'
Colors['Dragon'] = '#6F35FC'
Colors['Dark'] = '#705746'
Colors['Steel'] = '#B7B7CE'
Colors['Fairy'] = '#D685AD'


patch = []
for i in Colors:
	patch.append( mpatches.Patch(color=Colors[i], label=i) )
plt.legend(loc=10, ncol=3, borderaxespad=0., handles=patch)
plt.show()

###############################################################################################
Attack = defaultdict(list)
Defense = defaultdict(list)
HP = defaultdict(list) 
Speed = defaultdict(list) 
Type_Strength = defaultdict(list)

for index,row in new_df.iterrows():
	Attack[row['Type 1']].append( (row['Attack'] + row ['Sp. Atk'])/float(2) )
	Defense[row['Type 1']].append( (row['Defense'] + row ['Sp. Def'])/float(2) )
	HP[row['Type 1']].append( row['HP'] )
	Speed[row['Type 1']].append( row['Speed'] )

	Type_Strength[row['Type 1']].append( row['Total'] )

Types = []
for i in Attack:
	Types.append(i)


################################Scatter plot of Different Pokemons###############################
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in Types:
	ax.scatter( Attack[i], Defense[i], HP[i], c=Colors[i] )

ax.set_xlabel('Attack')
ax.set_ylabel('Defense')
ax.set_zlabel('HP')

plt.show()

##############################Type comparison Main Bar Graph######################################
for i in Types:
	Attack[i] = sum(Attack[i]) / float(len(Attack[i]))	
	Defense[i] = sum(Defense[i]) / float(len(Defense[i]))
	HP[i] = sum(HP[i]) / float(len(HP[i]))
	Speed[i] = sum(Speed[i]) / float(len(Speed[i]))


values = [HP[i] for i in HP]

ind = np.arange(4)  		# the x locations for the groups
width = 0.04      		# the width of the bars

fig, ax = plt.subplots()


num=0
for i in Types:
	ax.bar(ind + num*width, [Attack[i], Defense[i], HP[i], Speed[i]], width, color=Colors[i]) 
	num+=1

# add some text for labels, title and axes ticks
ax.set_xticks(ind + num*width / 2)
ax.set_xticklabels(('Attack', 'Defense', 'HP', 'Speed'))

plt.show()


##########################Visualization of Type Strengths#########################################
for i in Type_Strength:
	Type_Strength[i] = sum(Type_Strength[i]) / float(len(Type_Strength[i]))	
	print(i,"   ",Type_Strength[i])

Xloc = np.array( range(3) )
labels = ['Grass', 'Fire', 'Water']
values = [Type_Strength[i] for i in labels]
width = 0.5

barlist = plt.bar( Xloc, values, width=width )
barlist[0].set_color(Colors[labels[0]])
barlist[1].set_color(Colors[labels[1]])
barlist[2].set_color(Colors[labels[2]])
plt.xticks( Xloc, labels)
plt.show()



Xloc = np.array( range(5) )
labels = ['Dragon', 'Flying', 'Steel', 'Rock', 'Ice']
values = [Type_Strength[i] for i in labels]
width = 0.5

barlist = plt.bar( Xloc, values, width=width )
barlist[0].set_color(Colors[labels[0]])
barlist[1].set_color(Colors[labels[1]])
barlist[2].set_color(Colors[labels[2]])
barlist[3].set_color(Colors[labels[3]])
barlist[4].set_color(Colors[labels[4]])
plt.xticks( Xloc, labels)
plt.show()



Xloc = np.array( range(5) )
labels = ['Electric', 'Bug', 'Normal', 'Ground', 'Fighting']
values = [Type_Strength[i] for i in labels]
width = 0.5

barlist = plt.bar( Xloc, values, width=width )
barlist[0].set_color(Colors[labels[0]])
barlist[1].set_color(Colors[labels[1]])
barlist[2].set_color(Colors[labels[2]])
barlist[3].set_color(Colors[labels[3]])
barlist[4].set_color(Colors[labels[4]])
plt.xticks( Xloc, labels)
plt.show()


Xloc = np.array( range(5) )
labels = ['Ghost', 'Dark', 'Psychic', 'Fairy', 'Poison']
values = [Type_Strength[i] for i in labels]
width = 0.5

barlist = plt.bar( Xloc, values, width=width )
barlist[0].set_color(Colors[labels[0]])
barlist[1].set_color(Colors[labels[1]])
barlist[2].set_color(Colors[labels[2]])
barlist[3].set_color(Colors[labels[3]])
barlist[4].set_color(Colors[labels[4]])
plt.xticks( Xloc, labels)
plt.show()
