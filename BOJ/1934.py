def lcm(n1, n2):
    if n1==n2:
        return n1
    if max(n1,n2)%min(n1,n2)==0:
        return max(n1, n2)
    
    for i in range(2, min(n1,n2)+1):
        if n1%i == 0 and n2%i==0:
            return i*lcm(n1//i, n2//i)
    
    return n1*n2

def gcd(n1, n2):
    if n1%n2 != 0: return gcd(n2, n1%n2)
    else: return n2

T = int(input())
for _ in range(T):
    num1, num2 = map(int, input().split())
    print(num1*num2 // gcd(num1, num2))
    # Euclidean Algorithm
