n = int(input()) #soze pf tje cjessbpard
nums = list(map(int, input().split()))
nums.sort()
even = [i for i in range(1,n+1,2)]
odd = [i for i in range(2,n+1,2)]

a, b = 0, 0
for n, e, o in zip(nums, even, odd):
    a += abs(n-e)
    b += abs(n-o)

print(min(a,b))
