import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
N = int(sys.stdin.readline())

dp = [0] * (N+1)
dp[1] = 1; dp[2] = 2
for i in range(3,N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[N])
