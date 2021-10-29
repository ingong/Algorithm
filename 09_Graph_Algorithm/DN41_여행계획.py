# 부모 루트노드를 찾는 함수
# 동일한 루트노드에 속하는 집합 합치기
# 여행지의 수와 도시의 수 입력받고, parent 초기화
# 방문가능 인접행렬로 입력받기
# 동일한 루프노드에 속하는 집합 합치기
# 경로 입력받기
# 경로에 대해서 동일한 루트노드를 갖는지 확인하기
def find_parent(parent, x):
  if x != parent[x]:
    find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] == 1:
      union_parent(parent, i + 1, j + 1)

plan = list(map(int, input().split()))

result = True
for i in range(m - 1):
  if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
    result = False

if result:
  print('YES')
else:
  print('NO')
  