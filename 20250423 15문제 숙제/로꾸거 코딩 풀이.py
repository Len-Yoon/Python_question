# 로꾸거 코딩 풀이
str = input("팰린드롬인지 판단할 문자열을 입력하세요!")

#빈칸제거
str = str.replace(" ","").lower()
#문자열 거꾸로 출력
revers_str = str[::-1]

if str == revers_str:
    print(f"{str} == {revers_str} ==> 팰린드롬 입니다!")
else:
    print(f"{str} != {revers_str} ==> 팰린드롬이 아닙니다!")