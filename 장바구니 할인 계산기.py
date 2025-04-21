# 장바구니 할인 계산기

sum = 0
count = int(input("구매할 물건의 갯수를 입력하세요"))

for i in range(count):
    price = int(input("물건의 값을 입력하세요!"))

    if price >= 10000:
        sum += int(price * 0.9)
    else:
        sum += price

print(sum)