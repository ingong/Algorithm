from itertools import combinations

def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

def solution(nums):
    answer = 0
    candidate_list = list(combinations(nums, 3))
    for candidate in candidate_list:
        if(is_prime(sum(candidate))):
            answer += 1
    return answer