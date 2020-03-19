import pandas as pd

df = pd.read_csv("data/rtl_shapes.txt", header=0)
print(df.head())
results = df.loc[df["shape_id"]=="88_1_A"]
final_list = list()
for x, item in results.iterrows():
	# print(item)
	# print(str(item[["shape_pt_lat", "shape_pt_lon"]].values).replace(' ',','), end=', ')
	final_list.append([item["shape_pt_lat"], item["shape_pt_lon"]])

# print(final_list)
new_final_list = []
new_final_list = final_list
for x in list(reversed(final_list)):
	new_final_list.append([x[0], x[1]+0.001])
new_final_list.append(new_final_list[0])
print()
print(new_final_list)


# print(results)