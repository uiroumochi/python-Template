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
nCr = bikkuri.combi(n,r)
"""
#エラトステネスの篩
def sieve_prime_factorization(n):
    # 前処理: 最小素因数 (spf) 配列の構築
    spf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:  # i が素数の場合
            for j in range(i * i, n + 1, i):
                if spf[j] == j:  # 未代入の最小素因数を記録
                    spf[j] = i

    # 2 から n までの全整数を素因数分解
    result = {}
    for x in range(2, n + 1):
        factors = []
        temp = x
        while temp > 1:
            factors.append(spf[temp])
            temp //= spf[temp]
        result[x] = factors
        
    return result
