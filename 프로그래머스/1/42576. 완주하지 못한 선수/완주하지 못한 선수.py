from collections import Counter

def solution(participant, completion):
    # Counter -> 리스트/문자열 안에 있는 요소의 개수 자동으로 세어주는 메서드
    # 딕셔너리처럼 작동함 -> leo: 1, kiki: 1
    # 참가자 이름 카운팅
    p_cnt = Counter(participant)
    # 완주자 이름 카운팅
    c_cnt = Counter(completion)
    ans = p_cnt - c_cnt
    return list(ans.keys())[0]