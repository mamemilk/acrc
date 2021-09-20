pair_map = {}

def pair(x, y):
    global pair_map
    z = (x+y)*(x+y+1)//2 + x + 1
    pair_map[z] = (x,y)
    return z

# Left, Rightの探索の部分だけ早くすれば、現実時間に終わるかと思ったが、結局Pairでメモ化しないと終わらなかった。
def fast_left_right(z):
    if z == 0:
        return(0,0)

    if z in pair_map.keys():
        return pair_map[z]

    n = 0
    while z > ((n+1)*(n+2))//2:
        n += 1
    
    th = ((n+1) * (n+2)) // 2

    left  = n - (th - z)
    right = (th - z)

    return (left, right)   

def left(z):
    if z == 0:
        return 0

    if z in pair_map.keys():
        return pair_map[z][0]

    x = 0
    while x < z:
        y = 0
        while y < z:
            if pair(x,y) == z:
                return x
            y += 1
        x += 1

def right(z):
    if z == 0:
        return 0

    if z in pair_map.keys():
        return pair_map[z][1]

    x = 0
    while x < z:
        y = 0
        while y < z:
            if pair(x,y) == z:
                return y
            y += 1
        x += 1

def element(a, i):
    # l = left(a)
    # r = right(a)
    l, r = fast_left_right(a)
    loop = 1

    if i == 0:
        return 0

    while True:
        if loop == i:
            return l
        # l = left(r)
        # r = right(r)
        l, r = fast_left_right(r)
        loop += 1

def length(a):
    if a == 0:
        return 0

    l, r = fast_left_right(a)
    loop = 1

    while True:
        if r == 0:
            return loop
        l, r = fast_left_right(r)
        loop += 1

def sequence(x, k):
    p = pair(x, 0)

    loop = 1
    
    while True:
        if loop == k:
            return p
        p = pair(x, p)
        loop += 1

def replace(a, i, x):
    b = 0
    j = length(a)
    while j > 0:
        if j == i:
            b = pair(x,b)
        else:
            b = pair(element(a,j), b)

        j -= 1

    return b

#デバッグ用
def get_list(a):
    ans = []
    j = length(a)
    if j == 0:
        return ans

    l,r = fast_left_right(a)
    while j > 0:
        ans.append(l)
        l, r = fast_left_right(r)
        j -= 1
    return ans

#デバッグ用
def aprint(a):
    j = length(a)

    print("input is ", a)
    print("  length is ", j)

    l,r = fast_left_right(a)
    while j > 0:
        print("  ", l, " : ", ", ".join(list(map(str, get_list(l)))))
        l,r = fast_left_right(r)

        j -= 1
    print("  (0)")

#デバッグ用
def tuple2code(code):
    if type(code) is int:
        return code
    elif type(code) is tuple and len(code) == 1:
        return pair( tuple2code(code[0]), 0)
    else:
    #else if type(code) is tuple:
        return pair( tuple2code(code[0]), tuple2code(code[1:]) ) 

def is_code(p):
    k = element(p,1)
    m = element(p,2)
    S = element(p,3)
    n = length(S) + 1

    #print("is_code debug, ", k, m, S, n)

    pos = 1
    while(pos < n):
        if left(element(S, pos)) == 1:
            pos += 1
        elif left(element(S, pos)) == 2:
            pos += 1
        elif left(element(S, pos)) == 3:
            pos += 1
        elif left(element(S, pos)) == 4:
            pos += 1
        elif left(element(S, pos)) == 5:
            pos += 1
        elif left(element(S, pos)) == 6:
            pos += 1
        else:
            return False

    return True

def is_executable(p, x):
    k = element(p,1)
    if k == length(x) and is_code(p):
        return True
    else:
        return False

def comp(p, x):
    if is_executable(p,x):
        pass
    else:
        return

    k = element(p,1)
    m = element(p,2)
    S = element(p,3)
    n = length(S) + 1

    v = sequence(0,m)

    for i in range(1, k+1):
        v = replace(v, i, element(x,i))

    pc = 1

    while pc < n:
        if left(element(S,pc)) == 1:
            pc = element(element(S,pc),2)
        elif left(element(S,pc)) == 2:
            a = element(element(S,pc), 2)
            b = element(element(S,pc), 3)
            v = replace(v, a, b)
            pc += 1
        elif left(element(S,pc)) == 3:
            # print("comp debug")
            # aprint(v)
            a = element(element(S,pc), 2)
            b = element(element(S,pc), 3)
            v = replace(v, a, element(v,b))
            # aprint(v)
            pc += 1
        elif left(element(S,pc)) == 4:
            a = element(element(S,pc), 2)
            v = replace(v, a, element(v,a)+1)
            pc += 1
        elif left(element(S,pc)) == 5:
            a = element(element(S,pc), 2)
            v = replace(v, a, element(v,a)-1)
            pc += 1
            #print("type5 : decrement")
            #aprint(v)
        elif left(element(S,pc)) == 6:
            a = element(element(S,pc), 2)
            b = element(element(S,pc), 3)
            if element(v, a) > 0:
                pc = b
            else :
                pc += 1
    return element(v, 1)        


    
aprint(77826)
print( left(77826) )
print( right(77826) )
print( get_list(77826) )

aprint(2)
print( left(2) )
print( right(2) )
print( get_list(2) )

aprint(3)
print( left(3) )
print( right(3) )
print( get_list(3) )

print("##### test #####")
tashizan_code = tuple2code(((6,2,3), (1,6), (5,2), (4,1), (1,1)))
aprint(tashizan_code)
print( get_list(tashizan_code) )
print("this should be 0, ",is_code (tashizan_code) )

print("##### test #####")
tashizan = tuple2code((2, 2, ((6,2,3), (1,6), (5,2), (4,1), (1,1))))
aprint(tashizan)
print( get_list(tashizan) )
print("this should be 1, ",is_code (tashizan) )

# Pairの終端が０
arere = pair(2,pair(2,pair(113410085239160792121509200101,0)))
assert(arere == tashizan)

x = tuple2code((1,5))

print(get_list(x))

ans = comp(tashizan, x)
print(ans)


juu = tuple2code((10,))
aprint(juu)
aprint(pair(10,0))
guusuu = tuple2code((1, 2, ((3,2,1), (6,2,4), (1,9), (5,2), (6,2,7), (1,6), (5,2), (1,2))))

ans = comp(guusuu, juu)
print(ans)

