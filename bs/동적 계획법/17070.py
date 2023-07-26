import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# def solution():
#
#     # 1행 미리 처리하기 → (3) 과정
#     dp[0][0][1] = 1
#     for i in range(2, N):
#         if board[0][i] == 0:
#             dp[0][0][i] = dp[0][0][i - 1]
#
#     # 왜 1행과 1열을 제외하는지는 (3), (4) 과정에서 봤었죠?
#     for r in range(1, N):
#         for c in range(1, N):
#             # (5) 과정
#             # 대각선 파이프를 추가하는 과정
#             if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
#                 dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
#
#             # 가로, 세로 파이프를 추가하는 과정
#             if board[r][c] == 0:
#                 dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
#                 dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]
#
#     # 최종 결과 출력
#     print(sum(dp[i][N - 1][N - 1] for i in range(3)))
#
#
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
# solution()
def dfs(x,y,z):
    global cnt

    if x == N -1 and y == N-1:
        cnt +=1
        return

    # 대각선이동
    if x+1 < N and y + 1 < N:
        if graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0:
            dfs(x + 1, y + 1, 2)

    # 가로
    if z == 0 or z == 2:
        if y + 1 < N:
            if graph[x][y + 1] == 0:
                dfs(x, y + 1, 0)

    # 세로
    if z == 1 or z == 2:
        if x + 1 < N:
            if graph[x + 1][y] == 0:
                dfs(x + 1, y, 1)
cnt = 0
N = int(sys.stdin.readline())
# graph = [[] for _ in range(N)]
# for i in range(N):
#     graph[i] = list(map(int, input().split()))
graph = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]
print(graph)
dfs(0,1,0)

print(cnt)