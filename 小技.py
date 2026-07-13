#正整数nをk桁の2進数表記でprintする
def print_binary(n, k):
  print(f"{n:0{k}b}")



#階乗メーカー
class bikkurimaker:
    def __init__(self, mod: int):
        self.mod = mod
        self.cache = [1, 1]  # cache[i] は (i! % mod) を表す
    def extend_to(self, m: int):
        current_len = len(self.cache)
        if m < current_len:
            return
        last_val = self.cache[-1]
        for i in range(current_len, m + 1):
            last_val = (last_val * i) % self.mod
            self.cache.append(last_val)
    def get(self, k: int) -> int:
        if k >= len(self.cache):
            self.extend_to(k)
        return self.cache[k]
    def combi(self, n: int, r: int) -> int:
        if r < 0 or r > n:
            return 0
        numerator = self.get(n)
        denominator = (self.get(r) * self.get(n - r)) % self.mod
        denominator_inv = pow(denominator, self.mod - 2, self.mod)
        return (numerator * denominator_inv) % self.mod
"""  使い方
MOD = 10**9 + 7
bikkuri = bikkurimaker(MOD)
x! = bikkuri.get(x)
nCr = bikkuri.conbi(n,r)
"""

