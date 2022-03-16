#Import pakages

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import glob

#Path to files from Step1
paths_to_data = '/Users/raul/Documents/GitHub/ColonySelector/example_output/*.pkl'

paths_to_data  = glob.glob(paths_to_data)

#Name of samples (extract from file name)
names = ["clean_test_data1.pkl","clean_test_data1.pkl"]


#Extract the data

colony_all_files = []
colony_hold = []
colony_name = []

for i,name in enumerate(names):

	print(i+1,len(names))

	cnt = 0

	for path_crop in paths_to_data:

		file_name = path_crop.split('/')[-1]

		if name == file_name:

			print(path_crop)

			df_points = pd.read_pickle(path_crop)

			#Get all colony sizes

			for k,m in enumerate(np.unique(df_points['color'])):

				colony_hold.append(len(df_points.loc[df_points['color'] == m]))
				colony_name.append(file_name)
				    
	colony_all_files.append(colony_hold)


# Create the pandas DataFrame
d = {'values':colony_hold,'names':colony_name}
df = pd.DataFrame(data=d)

print(df, "\n")



# Plots
sns.set_theme(style="whitegrid")
ax = sns.boxplot(x="names", y="values", data=df)
locs=ax.get_xticks()
plt.title('Box plot');
plt.xlabel('Names')
plt.ylabel('Number of cells per colony')
plt.show()

sns.histplot(data=df,x = 'values', hue="names", log_scale=True)
plt.show()
