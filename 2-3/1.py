# 방법1

charge = int(input("가격 : "))

a = charge//500
charge = charge%500
b = charge//50
charge = charge%50
c = charge//10

print(a, b, c)

# 시간복잡도 : 6


#방법2

import time

n = 1260
count = 0

start_time = time.time()

coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n 
  n %= coin

print(count)

end_time = time.time()
print("time :", end_time - start_time)

#시간복잡도 : 4.6
