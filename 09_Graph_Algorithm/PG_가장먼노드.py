import heapq

def solution(n, edge):
    INF = int(1e9)
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for s, e in edge:
        graph[s].append((e, 1))
        graph[e].append((s, 1))
    
    
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance.count(max(distance[1:]))