t = 2
tests = [
    (5, [2, 2, 1, 1, 2, 4, 1, 2, 3, 4, 4, 1, 2, 3]),
    (4, [4, 1, 2, 3, 4, 4, 1, 2, 3, 4, 4, 1, 2, 3])
]

for i in range(t):
    n, shoes = tests[i]
    print(min_swaps(n, shoes))
