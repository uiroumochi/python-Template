#from functools import cache
#from collections import defaultdict,deque
#from sortedcontainers import SortedSet,SortedList
#import math,heapq

import sys,bisect
sys.setrecursionlimit(2000000)
input = lambda: sys.stdin.readline().rstrip()
def L():return list(map(int,input().split()))
def M():return map(int,input().split())
def M0():
  a = tuple(map(int,input().split()))
  return (x-1 for x in a) 
direct = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))

