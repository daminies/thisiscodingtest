# 큰 수의 법칙

# 방법1
# 시간복잡도 : 5.5
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

#정렬
num_list.sort()
first = num_list[n-1]
second = num_list[n-2]

result = 0

result = first*(m//k)*k + second*(m%k)
print(result)


# 방법2
# 시간복잡도 : 7.8
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

# 정렬
num_list.sort()
first = num_list[n-1]
second = num_list[n-2]

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result)
