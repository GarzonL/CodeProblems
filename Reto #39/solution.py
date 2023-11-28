
from math import sqrt
def get_triple_pitagorics(max_num: int) -> list:
    res = []
    for i in range(1, max_num):
        for j in range(1, i+2):
            a2 = j**2
            c2 = (i+2)**2
            b2 = get_b2(j, c2, i+2)
            if a2 + b2 == c2 and b2:
                res.append([j, int(sqrt(b2)), i+2])
    return res

def get_b2(a2, c2, max_num):
    for i in range(a2, max_num+1):
        if i**2 + a2**2 == c2:
            return i**2
        
    return 0

print(get_triple_pitagorics(10))