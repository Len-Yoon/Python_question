#카페 음료 총 가격 계산
orders = {"아메리카노":1500, "카페라떼":1800, "초코":2000, "바닐라라떼":2000}
menu = []
order = ""
price = 0

while True:
    order = input("메뉴를 입력하세요")
    if order == "끝":
        break
    elif order in orders:
        menu.append(order)
    else:
        print("잘못 입력했습니다.")

if menu != []:
    for i in menu:
        price += orders[i]

print(f"총 가격은 {price}원 입니다.")