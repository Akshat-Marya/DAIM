


def optimised_bubble_sort(array):
    for p in range(len(array)):
        flag = False
        for i in range(len(array)-p-1):
            #comp
            if array[i] > array[i+1]:
                # 10, 3 = 13, 3 = 13, 10 = 3, 10
                array[i] = array[i+1] + array[i]
                array[i+1] = array[i] - array[i+1]
                array[i]  = array[i] - array[i+1]
                #flag
                flag = True
            else:
                pass
        if not flag:
            break
    return array


def unoptimised_bubble_sort(array):
    for p in range(len(array)):
        for i in range(len(array)-1):
            #comp
            if array[i] > array[i+1]:
                # 10, 3 = 13, 3 = 13, 10 = 3, 10
                array[i] = array[i+1] + array[i]
                array[i+1] = array[i] - array[i+1]
                array[i]  = array[i] - array[i+1]
            else:
                pass
    return array
