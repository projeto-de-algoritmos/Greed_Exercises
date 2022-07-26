#problem knapsack https://codeforces.com/problemset/problem/1446/A


testCase = int(input())

for i in range (testCase):
    n, w = map(int, input().split())
    weights = list(map(int, input().split()))

    total = 0
    items = 0
    ans = []

    for c in range (len(weights)):
        if(weights[c] >= w/2 and weights[c] <= w):
            ans = [c+1]
            total = weights[c]
            items = 1
            break
        else:
            if(weights[c] + total <= w):
                total += weights[c]
                items += 1
                ans.append(c+1)
        if (total >= w/2):
            break
    
    if(total < w/2):
        print(-1)
    else:
        print(items)
        for c in range(items):
            if(c == items - 1):
                print(ans[c])
            else:
                print(ans[c], end=' ')
