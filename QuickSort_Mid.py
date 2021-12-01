import time


def partition(array, low, high):
    """
    The function takes in input array along with its indexes, assumes the middle element as a pivot
    around which rest of the array element will be sorted.
    :param array: Input array.
    :param low: First element index of array.
    :param high: Last element index of array.
    :return: Index of the pivot element after the array is sorted based on the pivot element.
    """
    mid_elem = (low + high) // 2
    # pivot (Element to be placed at correct position)
    pivot = array[mid_elem]

    # for j in range(high, low):
    while low <= high:
        # If current element from the end is greater than the pivot, skip it.
        while array[high] > pivot:
            high -= 1

        # If current element from the start is lesser than the pivot, skip it.
        while array[low] < pivot:
            low += 1

        if low <= high:
            # swap array[low] and array[high]
            array[low], array[high] = array[high], array[low]
            low += 1
            high -= 1

    # Return the lower index when it becomes greater than higher index of the array.
    return low


def quick_sort(array, low, high):
    """
    The function divides the array into sub-arrays based on the index of pivot elements.
    :param array: Array to be sorted.
    :param low: Minimum index of the array.
    :param high: Maximum index of the array.
    """
    if low < high:
        # p_index is index at which the traversing from left side crosses traversing from right side.
        # we split the array from this point.
        p_index = partition(array, low, high)

        quick_sort(array, low, p_index - 1)  # Before p_index
        quick_sort(array, p_index, high)  # After p_index


def sort_array_quick(arr):
    """
    The function will sort the input array using quick sort approach and return the time taken for sort.
    :param arr: Array to be sorted.
    :return: Time taken for sorting the array.
    """
    start_time = time.time()
    quick_sort(arr, 0, (len(arr) - 1))
    elapsed_time = (time.time() - start_time) * 1000
    return elapsed_time


def main():
    print("Use DriverSort.py to execute")

if __name__ == "__main__":
    main()