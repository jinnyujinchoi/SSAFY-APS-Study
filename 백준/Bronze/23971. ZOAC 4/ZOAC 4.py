# 풀이
def solve(H, W, N, M):
    # 20 - 8 - 10 + 4 를 어떻게 만들어 줄까!
    a = (W-1) // (M+1) + 1
    b = (H-1) // (N+1) + 1
    return a*b

# 입력
H, W, N, M = list(map(int, input().split()))
ans = solve(H, W, N, M)
print(ans)