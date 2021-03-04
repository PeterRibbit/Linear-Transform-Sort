import random
import math


##DATA ANALYSIS:
# what info about the set can we get in N operations or less?
def getav(lyst):
    sum = 0
    count = len(lyst)
    for i in range(count):
        sum = sum + lyst[i]
    return (sum/count)



# Outliers: returns a list of "outliers", defined as (?)

def is_outlier(datapoint, min_val, average_val, max_val):
    #magic goes here
    return False

def get_outliers(lyst, average_val, min_val, max_val):
    outliers = []
    for i in range(len(lyst)):
        if is_outlier(lyst[i], min_val, average_val, max_val):
            outliers.append(lyst[i])
            del lyst[i]
    return outliers


# Standard Deviation: ?

# Random Member Data Points: 
# (Use a randomly generated small subset of the data to determine the best
# sorting algorithm. Requires the unsupported assumption that the data subset
# is similar to the actual data - not true but maybe useful) 

def get_random_members(lyst, min_val, max_val, num_members):
    members = []
    num_entries = len(lyst)
    for i in range(num_members):
        sampled_from_lyst = random.randrange(1, num_entries)
        members.append(lyst[sampled_from_lyst])
        del lyst[sampled_from_lyst] # ensure no member is sampled twice. We will put these back in lyst later
    
    for i in range(num_members):
        lyst.append(members[i]) 
        #Simple implementation breaks stability. 
        #Copy the whole list and select and del from there for a stable sort.
    return members

def generate_transformation_from_members(members, min_val, max_val):
    transform = "magic!"
    # More magic. Generates some kind of transformation to fit the member data points.
    return transform



## TRANSFORMATIONS:
# other transformations useful for different data sets or better than the standard linear transformation

# Bent transform:
# data from min to average is transformed into ~ n/2 boxes, data from average to max is transformed into ~n/2 boxes. 
def bent_transform (lyst, min_val, average_val, max_val):
    
    return 
    
def lower_half_transform(lyst, min_val, average_val):
    return

def upper_half_transform(lyst, average_val, max_val):
    return


    
def simple_logarithmic_transform(entry, max_val, min_val, num_entries):  #WIP: how to approximate y=((e^cx)-1)/((e^c)-1)
    return math.floor(num_entries*(math.log10(entry-min_val))/(math.log10(max_val-min_val))) 