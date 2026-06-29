#n = int(input())
#n,q = map(int,input().split())

#単位元
#INF = 0                                # ←ここ変える！       

#処理内容(ex.最大最小 区間和)                  
def syori(a,b):          
  #return a+b                           # ←ここ変える！！

#変えない
N = 1
while N < n:
  N<<=1
segtree = [INF]*(2*N)

#一点更新
def OneUpdate(index,value): # ← 0_indexed
  index = index + N         # ← 1_indexed
  #segtree[index] += value    #加算更新
  #segtree[index] = value     #代入更新          ←ここも変える
  p = index
  while p > 1:
    p >>= 1
    left = p*2
    right = p*2 +1
    segtree[p] = syori(segtree[left],segtree[right])

#区間取得{x|l<=x<r}
def GetSection(l,r): 
  ansL = INF
  ansR = INF
  l += N
  r += N-1
  while l<=r:
    if l&1 :
      ansL = syori(ansL,segtree[l])
      l+=1
    if not(r&1):
      ansR = syori(segtree[r],ansR)
      r-=1
    l>>=1
    r>>=1
  return syori(ansL,ansR)


a = list(map(int,input().split()))


#取り込み
for i in range(n):
  segtree[N+i] = a[i]

#構成
for i in range(N-1,0,-1):
  left = i*2
  right = i*2+1
  segtree[i] = syori(segtree[left],segtree[right])
