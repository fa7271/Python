import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())


N = int(sys.stdin.readline())
array = []
for i in range(N):
    # x,y = map(int,input().split())
    # array.append((x,y))
    array.append(list(map(int,sys.stdin.readline().split())))
# print(array)
array.sort(key = lambda x: (x[1],x[0]))

for i in array:
    print(i[0], i[1])


