n = int(input())
a = list(map(int,input().split()))
INF = 0
N = 1
while N < n:
  N<<=1
segtree = [INF]*(2*N)

#取り込み
for i in range(n):
  segtree[N+i] = a[i]

#構成
for i in range(N-1,0,-1):
  left = i*2
  right = i*2+1
  segtree[i] = segtree[left]+segtree[right]

#処理内容(ex.最大最小 区間和)
def syori(array):
  return sum(array)
  
#一点更新
def OneUpdate(index,value): # ← 0_indexed
  index = index + N         # ← 1_indexed
  segtree[index] += value   #更新
  p = index
  while p > 1:
    p >>= 1
    left = p*2
    right = p*2 +1
    segtree[p] = syori([segtree[left],segtree[right]])

#区間取得{x|l<=x<r}
def GetSection(l,r): 
  use = []
  l += N
  r += N-1
  while l<=r:
    if l&1 :
      use.append(segtree[l])
      l+=1
    if not(r&1):
      use.append(segtree[r])
      r-=1
    l>>=1
    r>>=1
  return syori(use)
