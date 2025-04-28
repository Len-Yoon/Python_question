text = "{a([0,1],(1.2.3.4.5)}"

stack = []
for char in text:
    if char in ("(", "{", "["):
        stack.append(char)
    elif char in (")", "}", "]"):
        if not stack:
            print("오류: 닫는 괄호가 있는데 열림 괄호가 없음")
            break
        top = stack.pop()
        if (char == ")" and top != "(") or (char == "}" and top != "{") or (char == "]" and top != "["):
            print(f"오류: 괄호 짝이 안 맞음. 여는 괄호: {top}, 닫는 괄호: {char}")
            break
else:
    if stack:
        print("오류: 열림 괄호가 남아있음", stack)
    else:
        print("괄호 짝이 모두 맞음")
