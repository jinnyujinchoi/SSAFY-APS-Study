def solution(sizes):
    # 카드는 회전할 수 있으므로,
    # w가 최대,  h가 최소가 되도록 정렬
    arranged = [(max(w, h), min(w, h)) for w, h in sizes]
    # 정렬된 배열에서 최대너비, 최대높이 구하기
    max_w = max(w for w, h in arranged)
    max_h = max(h for w, h in arranged)
    # 구해야 하는건 최대너비 * 최대높이
    ans = max_w * max_h
    return ans