def solution(genres, plays):
    dic = {}
    for g, p in zip(genres, plays):
        if g in dic.keys():
            dic[g] += p
        else:
            dic[g] = p
        
    s_dic = sorted(dic, key= lambda x : dic[x], reverse = True)
    genres_play = [[*val, idx] for idx, val in enumerate(zip(genres, plays))]
    genres_play.sort(key = lambda x : x[1], reverse = True)
    
    answer = []
    for i in s_dic:
        count = 0
        for item in genres_play:
            if item[0] == i:
                answer.append(item[2])
                count += 1
            if count == 2:
                break
                
    return answer