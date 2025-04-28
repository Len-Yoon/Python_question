arr = []

while True:
    inputStr = input("i:라인 삽입, d:라인삭제, r:라인 변경, p:현재내용 출력, l:파일 입력, s:파일 출력, q:편집기 종료   => 원하는 명령문을 입력하세요")

    if inputStr == "i":
        num = input("삽입할 라인의 숫자를 입력하세요")
        str = input("입력할 문장을 입력하세요")
        arr.insert(num, str)
    elif inputStr == "r":
        num = input("변경할 행 번호를 입력하세요")
        str = input("변경할 문장을 입력하세요")
        arr[num] = str
    elif inputStr == "d":
        num = input("삭제할 라인의 숫자를 입력하세요!")
        arr.pop(num)
    elif inputStr == "p":
        print("현재 내용을 출력합니다")
        for line in arr:
            print(line)
    elif inputStr == "l":
        with open("test.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())
    elif inputStr == "s":
        with open("test.txt", 'w', encoding='utf-8') as f:
            for line in arr:
                f.write(line + "\n")
    elif inputStr == "q":
        break