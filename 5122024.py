
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    d=bin(n)
    count=0
    MAX=0
    for i in d:
        if i=='1':
            count+=1
        else:
            MAX = max(MAX,count)
            count = 0

print(max(MAX, count))
            

 