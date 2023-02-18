data = input()
result = []
value = 0

# 문자를 하나씩 확인
for x in data :
    if x.isalpha():
        result.append(x) # 알파벳인 경우 리스트에 삽입
    else:
        value += int(x) # 숫자는 따로 더해놓기

result.sort() # 알파벳을 오름차순으로 정렬

if value != 0: # 숫자가 하나라도 존재한다면
    result.append(str(value)) ## 가장 뒤에 삽입

print(''.join(result)) #최종 결과 리스트를 문자열로 변환하여 출력