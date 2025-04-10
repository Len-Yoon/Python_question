##지역별 인구 관련 문제
import random


def roll():
   return random.randint(100,1000)

data = []

area = ["서울","부산","대구","인천","광주","대전","울산","경기","강원","충북","충남","전북","전남","경북","경남","제주"]

for i in area:
    for j in range(2014,2026):
        data.append([i,j,roll()*10000])

for i in data:
    print("".join(f"[지역: {i[0]}, 년도: {i[1]}, 인구 수: {i[2]}]"))

print("")
print("")

## 예시 데이터 합
## 서울 년도 별 인구 차이수
for i in range(1,len(data)):
    if data[i][0] == "서울":
        print("".join(f"{data[i-1][1]}년도와 {data[i][1]}년도 {data[i][0]} 인구 차이 수: {data[i][2] - data[i-1][2]}"))

print("")
print("")

## 년도 별 총 인구 수:
for i in range(2014,2026):
    num = 0
    total = 0
    for l,j,k in data:
        if j == i:
            total += k
    print("".join(f"{i}년도 전체 인구 수: {total}"))

