import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

input = sys.stdin.readline
# input = int(sys.stdin.readline())

from math import factorial
n, k = map(int, input().split())
result = factorial(n) // (factorial(k) * factorial(n - k))
print(result % 10007)

N,M = map(int,input().split())
list_n = list()
list_m = list()


for i in range(N,0,-1):
    list_n.append(i)
for i in range(M,0,-1):
    list_m.append(i)

x = 1
y = 1
for i in range(0,M):
    y *= list_n[i]
    x *= list_m[i]
print((y // x) % 10007 )
