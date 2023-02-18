n, k = map(int, input().split()) # 25 3

result = 0

while True :
    # 나누어 떨어지지 않을 때 가장 가까운 맞아 떨어지는 값을 구하는 것
    target = (n // k) * k
    result += (n - target)
    n = target

    # n이 k보다 작아 더 이상 나눌 수 없을 때 반복문 탈출
    if n < k :
        break

    # k로 나누기
    result += 1
    n //= k

result += (n-1)
print(result)
