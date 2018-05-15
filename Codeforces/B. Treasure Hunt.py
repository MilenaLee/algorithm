def calc():
    string = input()

    import collections

    stringCounter = collections.Counter(string)
    maxi = max(stringCounter, key=stringCounter.get)

    if n == 1 and stringCounter[maxi] == len(string):
        return len(string)-1

    return min(len(string), stringCounter[maxi]+n)

n = int(input())
kuro = calc()
shiro = calc()
katie = calc()

if kuro > shiro and kuro > katie:
    print("Kuro")
elif shiro > kuro and shiro > katie:
    print("Shiro")
elif katie > kuro and katie > shiro:
    print("Katie")
else:
    print("Draw")
