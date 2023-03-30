def minimum_swaps(n, arr):
    # Count the occurrences of each shoe type
    count = {}
    for i in range(2*n):
        if arr[i] not in count:
            count[arr[i]] = 1
        else:
            count[arr[i]] += 1

    # Check if all shoes have a pair
    for key in count:
        if count[key] != 2:
            return -1

    # Iterate over the array and find misplaced shoes
    swaps = 0
    for i in range(2*n):
        if i%2 == 0 and arr[i] != arr[i+1]:
            # Find the right shoe and swap it
            for j in range(i+1, 2*n):
                if arr[j] == arr[i]:
                    arr[i+1], arr[j] = arr[j], arr[i+1]
                    swaps += 1
                    break

    return swaps

# Read the input
t = int(input())
for i in range(t):
    n, *arr = map(int, input().split())

    # Call the function and print the result
    result = minimum_swaps(n, arr)
    print(result)
