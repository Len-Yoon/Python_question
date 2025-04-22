# 더치페이 하기 풀이
human = ["김","백"]

price1 = 18000

print(f"1차 나온 비용:  {price1} // 먹은 사람: {human} // 더치페이비: {price1//len(human)}")

print("2차 고 와 장 합류")

human.extend({"고","장"})
price2 = 300000
print(f"2차 나온 비용:  {price2} // 먹은 사람: {human} // 더치페이비: {price2//len(human)}")

print("3차 백 과 장 이탈")
human.remove("백")
human.remove("장")

price3 = 50000
print(f"3차 나온 비용:  {price3} // 먹은 사람: {human} // 더치페이비: {price3//len(human)}")