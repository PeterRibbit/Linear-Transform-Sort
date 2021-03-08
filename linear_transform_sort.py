import math

# Global variable so we can add sorted sections
# Saves complexity because we don't need to flatten
sorted_list = []

#supporting functions

#gets min_val and max_val
def getmax_val(lyst):
    max_val = -math.inf
    for i in range(len(lyst)):
        if lyst[i] > max_val:
            max_val = lyst[i]
    return max_val

def getmin_val(lyst):
    min_val = math.inf 
    for i in range(len(lyst)):
        if lyst[i] < min_val:
            min_val = lyst[i]
    return min_val

# main functions for linear transform sort

def linear_transform(entry, max_val, min_val, num_entries):
    ret_val = math.floor(num_entries*(entry-min_val)/(max_val-min_val))
    # testing: print("transforming " + str(entry) + " to " + str(ret_val))
    return ret_val

def linear_transform_sort_helper(sublyst):
    global sorted_list
    num_entries = len(sublyst)
    if num_entries == 0:
        return # this bin has no contents
    if num_entries == 1:
        sorted_list.append(sublyst[0])
        return # sorting complete on this bin
    min_val = getmin_val(sublyst)
    max_val = getmax_val(sublyst)
    if min_val == max_val:
        for value in sublyst:
            sorted_list.append(value)
        return # sorting complete on this bin
    else: # more sorting is necessary if min_val != max_val and num_entries > 1
        bins = []
        # OPTIMIZATION: we sacrifice memory space to save complexity by creating all bins before we know if we need them.
        for i in range(num_entries + 1): # create n+1 bins
            bins.append([]) 
        for i in range(num_entries): # move members into bins
            cast_location = linear_transform(sublyst[i], max_val, min_val, num_entries)
            bins[cast_location].append(sublyst[i])
        for i in range(num_entries + 1): # recurse on each bin
            linear_transform_sort_helper(bins[i])

def lt_sort(lyst):
    global sorted_list
    sorted_list = []
    linear_transform_sort_helper(lyst)
    return sorted_list
