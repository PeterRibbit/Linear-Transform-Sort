import random
# import numpy -maybe later to run normally distributed data
from linear_transform_sort import lt_sort
from radixSort import radixSort
from quicksort import quicksort
from time import perf_counter
import string


#several different random data generators

def rand_int_data(to_add, min, max):
    lyst = []
    lyst.append(min)
    lyst.append(max)
    to_add -= 2 # we already added 2 values
    while to_add > 0:
        lyst.append(random.randint(min, max))
        to_add -= 1
    return lyst

def rand_nonint_data(to_add, min, max):
    lyst = []
    lyst.append(min)
    lyst.append(max)
    to_add -= 2 # we already added 2 values
    while to_add > 0:
        lyst.append(random.uniform(min, max))
        to_add -= 1
    return lyst
    
def linear_data(to_add, min, max):
    lyst = []
    lyst.append(min)
    for i in range(to_add-1):
        lyst.append(min + i*((max-min)/to_add))
    random.shuffle(lyst)
    return lyst

def squared_data(size, not_used, also_not_used):
    lyst = []
    not_used = not_used
    also_not_used = also_not_used
    for i in range(size):
        lyst.append(i^2)
    random.shuffle(lyst)
    return lyst

def factorial_data(size, not_used, also_not_used):
    lyst = []
    not_used = not_used
    also_not_used = also_not_used
    for i in range (size):
        if i == 0:
            lyst.append(1)
        else:
            lyst.append(lyst[i-1]*i)
    random.shuffle(lyst)
    return lyst



def flat_data(size, not_used, also_not_used):
    lyst = []
    not_used = not_used
    also_not_used = also_not_used
    for i in range(size):
        lyst.append(42)
        i=i # i is intended to be unused
    return lyst



''' # String sorting WIP
def string_data(filename):
    lyst = []
    #string input in, read space separated words. Include punctuation.
    return lyst
'''

def is_sorted(lyst):
    # return True if sorted (ascending order)
    lystLength = len(lyst)
    if (lystLength <= 1):
        return True
    prev_value = lyst[0]
    for i in range(lystLength):
        if lyst[i] < prev_value:
            return False
        prev_value = lyst[i]
    return True


global reps_left


def main():
    default_size = 100000
    default_min = 0
    default_max = 10000000000
    reps = 100
    print("We will compare  linear_transform_sort, quicksort, and timsort. \n")

    # Random int data
    print("Evaluating sorts with a random integer data set:")
    transform_sort_time = 0
    quicksort_time = 0
    timsort_time = 0
    
    reps_left = reps
    while reps_left > 0:
        # generate data
        lyst = rand_int_data(default_size, default_min, default_max)
        # time linear_transform_sort
        test = lyst.copy()
        start = perf_counter()
        test = lt_sort(test)
        transform_sort_time = perf_counter() - start
        # assert is_sorted(test)
        # time quicksort
        test = lyst.copy()
        start = perf_counter()
        test = quicksort(test)
        quicksort_time = perf_counter() - start
        # assert is_sorted(test)
        # time timsort
        test = lyst.copy()
        start = perf_counter()
        test.sort()
        timsort_dummy = test
        timsort_time = perf_counter() - start
        # assert is_sorted(test)
        reps_left -= 1
    # report average time
    
    print("Average time for linear_transform_sort: ", transform_sort_time/reps)
    print("Average time for quicksort: ", quicksort_time/reps)
    print("Average time for timsort: ", timsort_time/reps)

    # Sorted int data
    print("Evaluating sorts with a sorted integer data set:")
    transform_sort_time = 0
    quicksort_time = 0
    timsort_time = 0
    reps_left = reps
    while reps_left > 0:
        # generate data
        lyst.sort()
        # time linear_transform_sort
        test = lyst.copy()
        start = perf_counter()
        test = lt_sort(test)
        transform_sort_time = perf_counter() - start
        # assert is_sorted(test)
        # time quicksort
        test = lyst.copy()
        start = perf_counter()
        test = quicksort(test)
        quicksort_time = perf_counter() - start
        # assert is_sorted(test)
        # time timsort
        test = lyst.copy()
        start = perf_counter()
        test.sort()
        timsort_dummy = test
        timsort_time = perf_counter() - start
        # assert is_sorted(test)
        reps_left -= 1
    # report average time
    print("Average time for linear_transform_sort: ", transform_sort_time/reps)
    print("Average time for quicksort: ", quicksort_time/reps)
    print("Average time for timsort: ", timsort_time/reps)

    # Random double data
    print("Evaluating sorts with a random noninteger data set:")
    transform_sort_time = 0
    quicksort_time = 0
    timsort_time = 0
    reps_left = reps
    while reps_left > 0:
        # generate data
        lyst = rand_nonint_data(default_size, default_min, default_max)
        # time linear_transform_sort
        test = lyst.copy()
        start = perf_counter()
        test = lt_sort(test)
        transform_sort_time = perf_counter() - start
        # assert is_sorted(test)
        # time quicksort
        test = lyst.copy()
        start = perf_counter()
        test = quicksort(test)
        quicksort_time = perf_counter() - start
        # assert is_sorted(test)
        # time timsort
        test = lyst.copy()
        start = perf_counter()
        test.sort()
        timsort_dummy = test
        timsort_time = perf_counter() - start
        # assert is_sorted(test)
        reps_left -= 1
    # report average time
    print("Average time for linear_transform_sort: ", transform_sort_time/reps)
    print("Average time for quicksort: ", quicksort_time/reps)
    print("Average time for timsort: ", timsort_time/reps)

    # Flat distribution
    print("Evaluating sorts with a linear data set:")
    transform_sort_time = 0
    quicksort_time = 0
    timsort_time = 0
    reps_left = reps
    while reps_left > 0:
        # generate data
        lyst = linear_data(default_size, default_min, default_max)
        # time linear_transform_sort
        test = lyst.copy()
        start = perf_counter()
        test = lt_sort(test)
        transform_sort_time = perf_counter() - start
        # assert is_sorted(test)
        # time quicksort
        test = lyst.copy()
        start = perf_counter()
        test = quicksort(test)
        quicksort_time = perf_counter() - start
        # assert is_sorted(test)
        # time timsort
        test = lyst.copy()
        start = perf_counter()
        test.sort()
        timsort_dummy = test
        timsort_time = perf_counter() - start
        # assert is_sorted(test)
        reps_left -= 1
    # report average time
    print("Average time for linear_transform_sort: ", transform_sort_time/reps)
    print("Average time for quicksort: ", quicksort_time/reps)
    print("Average time for timsort: ", timsort_time/reps)
    
    # Perfect squares
    print("Evaluating sorts with a squared data set:")
    transform_sort_time = 0
    quicksort_time = 0
    timsort_time = 0
    reps_left = reps
    while reps_left > 0:
        # generate data
        lyst = squared_data(default_size, max, min)
        # time linear_transform_sort
        test = lyst.copy()
        start = perf_counter()
        test = lt_sort(test)
        transform_sort_time = perf_counter() - start
        # assert is_sorted(test)
        # time quicksort
        test = lyst.copy()
        start = perf_counter()
        test = quicksort(test)
        quicksort_time = perf_counter() - start
        # assert is_sorted(test)
        # time timsort
        test = lyst.copy()
        start = perf_counter()
        test.sort()
        timsort_dummy = test
        timsort_time = perf_counter() - start
        # assert is_sorted(test)
        reps_left -= 1
    # report average time
    print("Average time for linear_transform_sort: ", transform_sort_time/reps)
    print("Average time for quicksort: ", quicksort_time/reps)
    print("Average time for timsort: ", timsort_time/reps)
    
    # All duplicates
    print("Evaluating sorts with a uniform data set:")
    transform_sort_time = 0
    quicksort_time = 0
    timsort_time = 0
    reps_left = reps
    while reps_left > 0:
        # generate data
        lyst = flat_data(default_size, max, min)
        # time linear_transform_sort
        test = lyst.copy()
        start = perf_counter()
        test = lt_sort(test)
        transform_sort_time = perf_counter() - start
        # assert is_sorted(test)
        # time quicksort
        test = lyst.copy()
        start = perf_counter()
        test = quicksort(test)
        quicksort_time = perf_counter() - start
        # assert is_sorted(test)
        # time timsort
        test = lyst.copy()
        start = perf_counter()
        test.sort()
        timsort_dummy = test
        timsort_time = perf_counter() - start
        # assert is_sorted(test)
        reps_left -= 1
    # report average time
    print("Average time for linear_transform_sort: ", transform_sort_time/reps)
    print("Average time for quicksort: ", quicksort_time/reps)
    print("Average time for timsort: ", timsort_time/reps)
    timsort_dummy[1] = 0
    # Factorial data: don't use factorial data.
    return 0

main()

''' # Normal distribution data WIP
def rand_normal_data(size, average, standard_deviation):
    lyst = []
    for i in range(size):
        lyst.append(numpy.random.normal(100, 20))
        i=i # i is intended to be unused
    return lyst
'''