list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8]]


flattened_list = []


for sublist in list_of_lists:
    flattened_list.extend(sublist)

print(flattened_list)  
