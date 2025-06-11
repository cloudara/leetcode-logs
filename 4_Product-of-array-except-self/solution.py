#!/usr/bin/env python3
import os
import sys, threading, math
from collections import defaultdict, deque
from typing import List

# ====================== FAST I/O & PARSERS ======================
def read_tokens():
    return sys.stdin.read().split()

def setup_reader():
    it = iter(read_tokens())
    ni = lambda: int(next(it))
    nf = lambda: float(next(it))
    ns = lambda: next(it)
    # Multi parsers
    def nlist(n, f=int):
        return [f(next(it)) for _ in range(n)]
    def pair(f=int, g=int):
        return f(next(it)), g(next(it))
    def triple(f=int, g=int, h=int):
        return f(next(it)), g(next(it)), h(next(it))
    return ni, nf, ns, nlist, pair, triple

# ======================= HELPER FUNCTIONS =======================
def gcd(a, b): return math.gcd(a, b)
def lcm(a, b): return a // gcd(a, b) * b

def binary_search(lo, hi, cond):
    while lo < hi:
        mid = (lo + hi)//2
        if cond(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

def build_prefix(arr):
    P=[0]*(len(arr)+1)
    for i,v in enumerate(arr,1):
        P[i]=P[i-1]+v
    return P

def range_sum(P, l, r): 
    return P[r+1]-P[l]

def build_prefix2D(mat):
    n,m=len(mat),len(mat[0])
    P=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            P[i+1][j+1]=mat[i][j]+P[i][j+1]+P[i+1][j]-P[i][j]
    return P

def range_sum2D(P, x1,y1,x2,y2):
    return P[x2+1][y2+1]-P[x1][y2+1]-P[x2+1][y1]+P[x1][y1]

def dfs(u, adj, vis):
    vis.add(u)
    for v in adj[u]:
        if v not in vis: dfs(v, adj, vis)

def bfs(start, adj):
    q=deque([start]); vis={start}; order=[]
    while q:
        u=q.popleft(); order.append(u)
        for v in adj[u]:
            if v not in vis:
                vis.add(v); q.append(v)
    return order

class DSU:
    def __init__(self,n):
        self.p=list(range(n)); self.r=[0]*n
    def find(self,x):
        if self.p[x]!=x:
            self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a==b: return False
        if self.r[a]<self.r[b]: a,b=b,a
        self.p[b]=a
        if self.r[a]==self.r[b]: self.r[a]+=1
        return True

# ============================ SOLVE ============================
def solve():
    ni, nf, ns, nlist, pair, triple = setup_reader()
    t = ni() # Get number of test cases
    out = [] # Initialize output list
    for _ in range(t): # Read each test case
        n = ni() # Read number of elements
        arr = nlist(n) # Read the array of elements
        ans = productExceptSelf("", arr)
        out.append(str(ans))
    print("\n".join(out))

def productExceptSelf(self, nums: List[int]) -> List[int]:
    if( not nums or len(nums) == 0):
        return []
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res

    
# =========================== ENTRY ===========================
if __name__ == "__main__":
    LOCAL = True
    if LOCAL:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        sys.stdin = open(os.path.join(base_dir, 'input.txt'), 'r')
        sys.stdout = open(os.path.join(base_dir, 'output.txt'), 'w')
    threading.Thread(target=solve).start()
