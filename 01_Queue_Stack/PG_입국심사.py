def solution(n, times):
    left, right = 1, n * max(times)
    answer = 0
    
    while left  <= right:
        mid = (left + right) // 2
        people = 0
        
        for time in times:
            people += (mid // time)
            if people >= n:
                break
                
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
        print(answer, left, right)
    return answer