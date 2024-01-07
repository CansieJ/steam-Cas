def bubble(array, index, reverse=False):

    n = len(array)

    for i in range(n):

        already_sorted = True

        for j in range(n - i - 1):

            if array[j][index] > array[j + 1][index]:

                array[j][index], array[j + 1][index] = array[j + 1][index], array[j][index]

                already_sorted = False

        if already_sorted:

            break

    if reverse == True:
        return array[::-1]
    else: return array
