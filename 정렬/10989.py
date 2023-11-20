import sys
N = int(input())
count = {}
for _ in range(N):
    n = int(sys.stdin.readline())
    count[n] = count.get(n, 0) + 1
for i in range(1, 10001):
    try:
        for j in range(count[i]):
            print(i)
    except KeyError:
        continue
