#from collections import defaultdict,deque
#from sortedcontainers import SortedSet
import sys,bisect
sys.setrecursionlimit(2000000)
input = lambda: sys.stdin.readline().rstrip()
def L():return list(map(int,input().split()))
def M():return map(int,input().split())
direct = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))

