## Greedy Approach ##
def coin_changing(L, amount):
    denominations = []
    i = 0 
    while(i < len(L)):
        num = int(amount/L[i])
        amount = amount - num * L[i]
        denominations.append(num)
        i += 1
    return denominations, amount

L = [500, 100, 50, 20, 10, 5, 2, 1]
# print(len(L))
den = coin_changing(L, 757)
# print(den)

## Dynamic Programming ##
def fac(n):
    if n == 1:
        return 1
    else:
        return fac(n-1)*n
    
# print(fac(1))
# print(fac(5))

def fac1(n):
    fac_num = []
    if n == 1:
        fac_num.append(1)
    else:
        fac_num.append(1)
        for i in range(1, n):
            fac_num.append(fac_num[i-1]*(i+1))
    return fac_num[-1]

print(fac1(5))
