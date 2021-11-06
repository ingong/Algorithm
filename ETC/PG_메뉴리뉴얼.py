# 다시 푼 풀이
from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    for count in course:
        candidate = []
        for order in orders:
            target = list(combinations(sorted(order), count))
            target = list(map(lambda x: ''.join(x), target))
            candidate += target
        candidate_list = Counter(candidate).most_common()
        answer += [menu for menu, ctx in candidate_list if ctx > 1 and ctx == candidate_list[0][1]]
    return sorted(answer)

# 답지 보고 푼 풀이
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        
        sorted_candidates = Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)