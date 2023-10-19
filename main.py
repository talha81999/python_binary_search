given_list = [1, 2, 4, 5, 6, 8]  # It should be sorted for binary search to work correctly


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


number = int(input("Please enter the number to search for: "))
result = binary_search(given_list, number)

if result != -1:
    print(f"The number {number} was found at index {result}.")
else:
    print(f"The number {number} was not found in the list.")
