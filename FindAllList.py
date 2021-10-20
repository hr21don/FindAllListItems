def index_all(search_list, item):
    indices = list() # empty list
    for i in range(len(search_list)): #iterate through each index number over the length of the list
        if search_list[i] == item: # check to see if item at each index is equal to the item searched for
            indices.append([i]) # append that index to the list of indices 
        elif isinstance(search_list[i], list): #check to see if the item was a list
                for index in index_all(search_list[i], item): #recursively search that sublist for the item
                    indices.append([i]+index) #for loop to append higher-level indicies 
    return indices
