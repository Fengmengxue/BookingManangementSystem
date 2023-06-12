n, m = map(int, input().split())

a = [i for i in range(1,n+1)]
# print(a)

l = []
for i in range(n):  # 输入p q
    l.append(list(map(int, input().split())))

for i in range(n):
    if l[i][0] == 0:
        j = l[i][1]
        temp = a[0:j]
        temp.sort(reverse=True)
        if j<n:
            a = temp + a[j:]
        else:
            a = temp
    if l[i][0] == 1:
        j = l[i][1]
        temp = a[j-1:]
        temp.sort()
        a = a[:j-1] + temp
# print(a)
for i in range(n):
    print(a[i], end=' ')
