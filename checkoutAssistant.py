#problem checkoutAssistant https://codeforces.com/problemset/problem/19/B

import math

n = int(input())

ans = [float() * (n+1)]
ans[0] = 0

for i in range(n):
    t, c = map(int, input().split())
    
    for j in range(n-1, -1, -1):
        w = min(j + t + 1, n)
        ans[w] = min(ans[w], ans[j]+c)

print(ans[n])