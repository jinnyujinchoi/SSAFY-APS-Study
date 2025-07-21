# 풀이
def solve(arr):
    # cnt(뒤로 물러선 횟수) 초기화
    cnt = 0
    # 차례대로 순회를 하자 (i번째 부터)
    for i in range(1, 21):
        switch = arr[i] # 바꿔줄 사람 인덱스
        # 나로부터 앞 까지의 범위 (키 큰 사람 찾기)
        for c in range(1, i):
            # 앞에 키가 큰 사람이 있다면
            if arr[c] > arr[i]: # 키 큰 사람 찾았다!
                # switch 앞에서부터 뒤로 이동
                for s in range(i, c, -1):
                    arr[s] = arr[s-1]
                    cnt += 1 # 뒤로 간 횟수 추가
                # 가장 앞 사람의 앞으로 이동
                arr[c] = switch
        continue
    return cnt

# 입력
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    ans = solve(arr)

    print(tc, ans)
