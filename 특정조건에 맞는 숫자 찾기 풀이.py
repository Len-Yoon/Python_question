#특정조건에 맞는 숫자 찾기 풀이

arr = [1,2,3,5, 9,13,15, 21]
question = []

for i in arr:
    if i % 3 == 0  and i % 2 == 1:
        question.append(i)

print(question)