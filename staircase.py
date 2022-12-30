#Question - https://www.hackerrank.com/challenges/staircase/


#!/bin/python3

import math
import os
import random
import re
import sys


def staircase(n):
    for i in range(0,n):
        for j in range(0,n):
            if i + j >= n-1:
                print("#",end='') 
            else:
                print(" ",end='')
        print("\r")

if __name__ == '__main__':
    n = int(input())

    staircase(n)
    


    '''    
    Output
     #
    ##
   ###
  ####
 #####
######

'''
    