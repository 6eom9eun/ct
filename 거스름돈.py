n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array :
    count += n // coin
    n %= coin

print(count)

#시간 복잡도 O(K) #K는 화폐 종류
