#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if N//2==1:
        print("Weird")
    if N//2==0 and N in range(2,6):
        print("Not Weird")

