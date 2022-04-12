def solution(id_list, report, k):
    answer = []
    emailCnt = {}
    reportMember = {}
    
    for i in id_list:
        emailCnt[i] = 0
        reportMember[i] = set()         # i를 신고한 사용자를 중복 허용하지 않기위해 value를 set으로 초기화
        
    for i in report:
        a, b = i.split()
        reportMember[b].add(a)
    
    for i in id_list:
        if len(reportMember[i]) >= k:   # set에 들어가있는 사용자가 k명 이상일 경우(신고한 사람이 k명 이상일 경우)
            for j in reportMember[i]:
                emailCnt[j] += 1        # set에 들어가있는 사용자의 emailCnt +1
    answer = list(emailCnt.values())
    
    return answer
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))