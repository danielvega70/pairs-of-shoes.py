def min_swaps(n, shoes):
    pairs = {}
    for i in range(2*n):
        if shoes[i] not in pairs:
            pairs[shoes[i]] = []
        pairs[shoes[i]].append(i)
    
    swaps = 0
    for i in range(1, n+1):
        left, right = pairs[i]
        if left%2 == 0:
            pair = left + 1
        else:
            pair = left - 1
        if pair != right:
            pairs[shoes[pair]], pairs[shoes[right]] = pairs[shoes[right]], pairs[shoes[pair]]
            shoes[pair], shoes[right] = shoes[right], shoes[pair]
            swaps += 1
    
    return swaps

t = int(input())
for _ in range(t):
    n, shoes = input().split()
    n = int(n)
    shoes = [int(x) for x in shoes]
    print(min_swaps(n, shoes))
