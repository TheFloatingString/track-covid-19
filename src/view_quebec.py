import geopandas
import matplotlib.pyplot as plt
import numpy as np


data = geopandas.read_file("data/regions_quebec.shp")
data = data.to_crs(epsg=4326)
print(data.head())
print(data.shape)
print(data.columns)

return_dict = dict()
for index, row in data.iterrows():
	final_list = []
	print(index)
	try:
		coordinates = data.geometry.iloc[index].exterior.coords
		# for x in coordinates:
			# reversed_list = list(reversed(x))
			# final_list.append(reversed_list)
		return_dict[index] = coordinates
	except:
		pass
		# coordinates = data.geometry.iloc[index].coords

# print(len(data.geometry.iloc[0].exterior.coords))

region_index = 4

np.savetxt('results.csv', return_dict[region_index], delimiter=',')

x = [x[0] for x in return_dict[region_index]]
y = [x[1] for x in return_dict[region_index]]



plt.plot(x,y)
plt.show()
