
import itertools
A=list(map(int,input().split()))
B = list(map(int, input().split()))

c = list(itertools.product(A, B))

for x in c: 
    print(x, end=" ")