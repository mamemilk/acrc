
import math

def factorize(n):
    res = []
    tmp = n
    for i in range(2,int(math.sqrt(n))+1):
        count = 0
        while tmp % i == 0:
            tmp = tmp // i
            count += 1
        if count != 0:
            res.append((i,count))
        
    if tmp!=1:
        res.append((tmp,1))
    
    if len(res)==0:
        res.append((n,1))

    return res


if __name__ == '__main__':
    print(factorize(10))
    print(factorize(25))
    