N = int(input())
numbers = []
for i in range(N):
  numbers.append(int(input()))

answer = []
for n in numbers:
  if n != 0:
    answer.append(n)
  else:
    answer.pop()

print(sum(answer))