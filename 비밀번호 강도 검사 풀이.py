# 비밀번호 강도 검사 풀이

password = input()
score = 0
arr = ["길이","소문자","대문자","숫자"]

if len(password) >= 8:
     score += 2
     arr.remove("길이")
if any(i.isdigit() for i in password):
    score += 2
    arr.remove("숫자")
if any(i.islower() for i in password):
    score += 1
    arr.remove("소문자")
if any(i.isupper() for i in password):
    score += 1
    arr.remove("대문자")

if score >= 6:
    print("비밀번호 강도: 강함")
elif score >= 4:
    print("비밀번호 강도: 보통")
else:
    print("비밀번호 강도: 약함")

if arr != 0:
    for i in arr:
        print("길이 8자 미만") if i == "길이" else None
        print("숫자 미포함") if i == "숫자" else None
        print("소문자 미포함") if i == "소문자" else None
        print("대문자 미포함") if i == "대문자" else None
