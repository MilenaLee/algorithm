n, m = map(int, input().split())

import collections
s = collections.defaultdict(list)
l = [0 for _ in range(m)]

for i in range(n):
    temp = input()
    for j,val in enumerate(temp):
        if val == '1':
            s[i].append(j)
            l[j] += 1

for i in range(n):
    flag = 0
    for val in s[i]:
        if l[val] - 1 == 0:
            flag = 1
            continue
    if flag == 0:
        break
        
if flag == 0:
    print("YES")
else:
    print("NO")
