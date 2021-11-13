def solution(lottos, win_nums):
    rank = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}
    zero_count = lottos.count(0)
    matches = sum([1 for lotto in lottos if lotto in win_nums])
        
    return [rank.get(matches + zero_count), rank.get(matches)]