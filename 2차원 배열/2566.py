arr = []
for i in range(9):
    arr = arr + list(map(int, input().split()))

print(max(arr))
print((arr.index(max(arr)) // 9 + 1), (arr.index(max(arr)) % 9 + 1))


arr1 = []
for i in range(9):
    arr1.append(list(map(int, input().split())))

maxN = -1
mi = 0
mj = 0
for i in range(len(arr1)):
    for j in range(len(arr1[0])):
        if arr1[i][j] > maxN:
            maxN = arr1[i][j]
            mi = i+1
            mj = j+1
print(maxN)
print(mi, mj)
