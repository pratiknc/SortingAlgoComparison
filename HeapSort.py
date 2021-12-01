import time

def heapify(arr, n, i):
    """
    The function helps to maintain the properties of a heap data structure, given the input array.
    :param arr: Input array
    :param n: Size of the heap
    :param i: Root of heap indexed at i.
    """
    # Find smallest among root and children
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] > arr[l]:
        smallest = l
    if r < n and arr[smallest] > arr[r]:
        smallest = r

    # If root is not smallest, swap with smallest and continue heapifying
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def heapsort(arr, sorted_arr):
    n = len(arr)

    # Build min heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        sorted_arr.append(arr[0])
        arr[0] = arr[i]
        arr = arr[0:i]
        # Heapify root element
        heapify(arr, i, 0)


def sort_array_heap(arr):
    """
    The function takes an input array, sorts it using heap sort approach and calculates the time taken for the sort.
    :param arr: The input array.
    :return: The time taken for sorting the array.
    """
    sorted_arr = []
    start_time = time.time()
    heapsort(arr, sorted_arr)
    elapsed_time = (time.time() - start_time) * 1000
    return elapsed_time


def main():
    print("Use DriverSort.py to execute")

if __name__ == "__main__":
    main()