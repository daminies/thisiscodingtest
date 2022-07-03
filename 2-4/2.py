# 답안1 -> 내가 생각한 답안
n = int(input())
# HH:MM:SS
# 03, 13, 23, 30, 31~39, 43, 53 -> 6경우 60-15 = 45
# 초에 하나라도 들어가 있는경우 + 분에 하나라도 들어있는경우 + 시간에 하나라도 들어있는경우 - 중복
# 전체경우의 수 - 3이 하나도 안들어있는경우 

# 3~12시 까지는 54*54*(n-1)
# 13시~22시 까지는 54*54*(n-2)
# 23시~24시 까지는 54*54*(n-3)


if n<3:
  sum = 45*45*(n+1)
elif (n>=3)and(n<13):
  sum = 45*45*(n)
elif (n>=13)and(n<23):
  sum = 45*45*(n-1)
else:
  sum = 45*45*(n-2)

sum = (n+1)*60*60 - sum

print(sum)


---------------------------------
# 예제답안
h = int(input())

count = 0
for i in range(h +1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)
