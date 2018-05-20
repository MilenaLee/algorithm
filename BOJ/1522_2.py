import collections

string = input()

location = collections.Counter(string)
missing = location['b']
N = len(string)
string += string
res = missing
        
for idx in range(N):
    if string[idx] == 'b':
        temp = 0
        for i in range(idx, idx+missing):
            if string[i] == 'a':
                temp += 1
        res = min(res, temp)

print(res)    
