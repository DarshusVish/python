def recursive_sort(data):
    return sorted(data)

def minimum_absolute_diff_pairs(n, arr):
    if n!= len(arr):
        return "invalid data"

    min_abs_dist = abs(arr[0] - arr[1])
    for i in range(1,n-1):
        min_ab = abs(arr[i] - arr[i+1])
        if min_ab < min_abs_dist:
            min_abs_dist = min_ab
    data = []
    for i in arr:
        for j in range(0,n):
            if abs(arr[j] - i) == min_abs_dist:
                data.append([i, arr[j]])
    print(min_abs_dist)
    print(data)
    data = [tuple(recursive_sort(da)) for da in data]
    data.sort()
    x = sorted(list(set(data)))
    for f,s in x:
        print(f"{f} {s}")

minimum_absolute_diff_pairs(4,[4,2,1,3])
