#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    count = 0
    
    min1 = 100000
    min2 = 100000
    for i, p in reversed(list(enumerate(q, 1))):
        if p - i > 2:
                print("Too chaotic")
                return ;
            
        if p > min2:
            count += 2
        elif p > min1:
            count += 1
            
        if p < min1:
            min1, min2 = p, min1
        elif p < min2:
            min2 = p
            
        
        
    print(count)
    
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
