#n = int(input())
#n,q = map(int,input().split())
#変えない
BIT = [0]*(n+1)


#一点加算
def OneUpdate(index,value): # ← 0_indexed
  index += 1                # ← 1_indexed
  while index <= n:
    BIT[index] += value
    index += index&(-index)


#前から{0<=x<=r}の取得
def GetPrefix(r): # ← 0_indexed
  r += 1          # ← 1_indexed
  ans = 0
  while r:
    ans += BIT[r]
    r -= r&(-r)
  return ans


#区間取得{l<=x<r}
def GetSection(l,r):
  return GetPrefix(r-1)-GetPrefix(l-1)


a = list(map(int,input().split()))
#構成
for i in range(n):
  OneUpdate(i,a[i])

