def solution(n):
    return int("".join(list(reversed(sorted(str(n))))))

print(solution(118372))