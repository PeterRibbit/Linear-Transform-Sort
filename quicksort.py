def quicksort(lyst):
    # sorts lyst and returns lyst. lyst is a list of integers
    size = len(lyst)
    quicksort_helper(lyst, 0, size - 1)
    return lyst

def quicksort_helper(lyst, low, high):
    if (low >= high): #base
        return
    else:
        # we will use the midpoint as the pivot in each case
        mid = partition(lyst, low, high)
        quicksort_helper(lyst, low, mid)
        quicksort_helper(lyst, mid+1, high)


def partition(lyst, low, high):
    # each partitioning step makes the partitioned part of the list more sorted
    mid = ((low + high) // 2)
    pivot_val = lyst[mid]

    while True: # run until the break
        # on the high side, move past high values until one is too low
        while (lyst[high] > pivot_val):
            high -= 1

        # on the low side, move past low values until one is too high
        while (lyst[low] < pivot_val):
            low += 1

        if (low >= high): # exit case - partitioning is complete
            break

        lyst[high], lyst[low] = lyst[low], lyst[high]   # move both values to a less wrong place
        low += 1
        high -= 1 # reset for next loop if necessary
    return high