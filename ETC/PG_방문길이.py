def isValidMove(x, y):
    return (0 <= x <= 10) and (0 <= y <= 10)

def solution(dirs):
    answer = 0
    direction = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L':(-1, 0)}
    opposite = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
    
    graph = [[[] for _ in range(11)] for _ in range(11)]
    coordinate = [(5, 5)]
    
    for dir in dirs:
        x, y = coordinate.pop() 
        dx, dy = direction[dir]
        X, Y = x + dx, y + dy
        if isValidMove(X, Y):
            if (dir not in graph[x][y]) and (opposite[dir] not in graph[X][Y]):
                graph[x][y].append(dir)
                graph[X][Y].append(opposite[dir])
                answer += 1
            coordinate.append((x + dx, y + dy))
        else:
            coordinate.append((x, y))
    return answer


# 다른 사람 풀이
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2