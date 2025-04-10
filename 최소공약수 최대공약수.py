import random


##임의의 숫자

def roll():
    return random.randint(2, 1000)


answer = []

##임의의 숫사 2부터 1000사이 추출
for i in range(10):
    arr = []
    a = roll()
    arr.append(a)

    num = []
    for j in range(2, a + 1):
        if a % j == 0:
            num.append(j)
    max_num = max(num)
    min_num = min(num)

    arr.append(min_num)
    arr.append(max_num)
    answer.append(arr)

for i in answer:
    print("".join(f"뽑은 숫자:{i[0]}  최소 약수: {i[1]}  최대 약수: {i[2]}"))