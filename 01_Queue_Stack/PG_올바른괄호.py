# open 이라면 그냥 넣어줌
# close 라면 무조건 Open 이 있어햐 매칭이 됨. 따라서 stack 이 없으면 False 를 반환, 있다면 stack 에서 제거
# stack 이 남아 있다면 짝이 다 지어지지 못한 것을 의미하므로, stack 이 빈 배열인지 여부에 따라서 Boolean 반환

from collections import deque
def solution(s):
    s_list = deque(s)
    stack = []
    
    while s_list:
        bracket = s_list.popleft()
        if bracket == '(':
            stack.append(bracket)
        else:
            if not stack:
                return False
            stack.pop()
    
    
    return False if stack else True