



def insertion_sort(array):

    for i in range(len(array)-1):
        #check
        if array[i] > array[i+1]:
            # swap all behind it
            for j in range(i+1, 0, -1):
                if array[j] < array[j-1]:
                    array[j-1], array[j] = array[j], array[j-1]
    return array
            