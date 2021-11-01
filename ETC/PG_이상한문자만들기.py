def solution(s):
    answer = []
    for char in s.split(" "):
        answer.append("".join([c.upper() if idx % 2 == 0 else c.lower() for idx, c in enumerate(char)]))
    return (" ").join(answer)