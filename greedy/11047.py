n, k = map(int, input().split())


arr=[]

for i in range(n):
  j = int(input())
  arr.append(j)

count = 0

while(n>0 and k>0):
    count += k//arr[n-1]
    k %= arr[n-1]
    n -= 1

print(count)