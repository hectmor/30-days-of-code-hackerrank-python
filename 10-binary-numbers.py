#!/bin/python3

import math
import os
import random
import re
import sys




def lenli(n):
    i = n
    bina =[]
    while i//2>=1:
        bina.append( i%2)
        i = i//2
    bina.insert(n,1)
    
    bina.reverse()

    ran=len(bina)
    conte = 1
    coli = []
    for li in range(ran):
        if bina[li] == 1:
            coli.append(conte)
            conte+=1
        else:
            conte=1
    print(max(coli))


if __name__ == '__main__':
    n = int(input().strip())
    
lenli(n)
