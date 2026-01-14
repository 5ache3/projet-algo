

def tri_par_selection(T):
    n=len(T)
    for i in range(n-1):
        min_=i
        for j in range(i+1,n):
            if T[j] < T[min_]:
                min_=j
        if min_ !=i:
            T[min_],T[i]=T[i],T[min_]
    return T


def merge(a,b):
    c=[]
    while a and b :
        if a[0]>b[0]:
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)

    while a:
        c.append(a[0])
        a.pop(0)

    while b:
        c.append(b[0])
        b.pop(0)
    return c

def merge_sort(T):
    n=len(T)

    if n == 1:
        return T
    
    left_half=T[:n//2]
    right_half=T[n//2:]

    a=merge_sort(left_half)
    b=merge_sort(right_half)

    return merge(a,b)

import random
import time
n=5_0000
liste=[random.randint(-10**2,10**2) for i in range(n)]
liste_c=liste.copy()
start=time.time()
tri_par_selection(liste)
end=time.time()
print(f"tri par selection avec {n} elements demande {end-start} s")
start=time.time()
merge_sort(liste_c)
end=time.time()
print(f"tri par fusion avec {n} elements demande {end-start} s")