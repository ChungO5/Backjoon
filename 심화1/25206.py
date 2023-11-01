L = []
for i in range(20):
    l = list(input().split())
    l[1] = float(l[1])
    L.append(l)

grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5,
         'B0': 3.0, 'C+': 2.5, 'C0': 2.0,
         'D+': 1.5, 'D0': 1.0, 'F': 0.0, }
credit = 0.0
grades = 0.0

for i in L:
    if i[2] != 'P':
        credit += i[1]
        grades += i[1] * grade.get(i[2])

print(grades/credit)
