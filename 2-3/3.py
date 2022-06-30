# 숫자 카드 게임
n, m = map(int, input().split())

mylist=[0 for _ in range(n)]
newlist = []

for i in range(n):
    mylist[i]=list(map(int, input().split()))

for j in range(n):
  mylist[j].sort()
  newlist.append(mylist[j][0])

newlist.sort()
print(newlist[n-1])
