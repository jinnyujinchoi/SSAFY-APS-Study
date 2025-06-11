def solution(array, commands):
    ans = []
    # 커맨드 내부를 순회하자
    for i in range(len(commands)):
        # 변수 지정 s, e, k
        s = commands[i][0] - 1
        e = commands[i][1]
        k = commands[i][2] - 1
        # 새로운 배열 정렬
        a2 = sorted(array[s:e])
        # ans에 추가
        ans.append(a2[k])
    return ans