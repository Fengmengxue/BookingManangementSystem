def quan(mid):
    for i in range(mid,n):
        if i+mid <=n:
            if (sum1[i] - sum1[i - mid] <= s and sum1[i + mid] - sum1[i]<=s):
                return 1
    return 0
sum1 = [0]
sum2 = 0
n,s = map(int,input().split())
list1  = list(map(int,input().split()))
for i in range(0,n):
    sum2 += list1[i]
    sum1.append(sum2)
l = 1
r = n//2
while(l<=r):
    mid = (l+r) // 2
    if quan(mid):
        l = mid +1
        k  = mid
    else:
        r = mid - 1
print(2*k)