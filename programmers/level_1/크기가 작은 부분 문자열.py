def solution(t, p):
    answer = 0
    sliced_list = [t[i:i+len(p)] for i in range(0, len(t))]
    
    for i in sliced_list:
        if i <= p and len(i) == len(p):
            answer += 1

    return answer