N = int(input())
L = [input() for i in range(N)]
for i in sorted(set(L), key=lambda x: (len(x), x)):
    print(i)
