# 잘 이해안가니까 다시보자 

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
# ord함수는 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환

#나이트가 이동할 수 있는 8가지 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2,1), (1, 2), (-1, 2), (-2, 1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인 
result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result)
