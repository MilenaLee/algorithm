def _get(idx):
    res = 0
    while idx > 0:
        res += fenwick[idx]
        idx &= (idx-1)
    return res
    
def get(start, end):
    return _get(end) - _get(start)

import collections

string = input()
string += string
fenwick = [0 for _ in range(len(string)+1)]
location = []

for idx, val in enumerate(string, 1):
    if val == 'b':
        location.append(idx)
        while idx < len(fenwick):
            fenwick[idx] += 1
            idx += (idx & (-1*idx))

res = 0
N = len(location)//2

for i in range(len(location)//2):
    idx = location[i]
    res = max(res, get(idx-1, idx+N-1))
    
print(N-res)
