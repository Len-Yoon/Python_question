import random

#숫자야구 게임 풀이
quest_num = random.randint(1,999)
input_num = 0
count = 1;

while True:

    input_num = int(input("1부터 999까지의 숫자를 넣어주세요"))
    if quest_num == input_num:
        print("strike!!!")
        break
    elif repr(input_num) in repr(quest_num):
        print("ball!!!")
    else:
        if count >= 3:
            print(f"3OUT!!! game over 정답: {quest_num}")
            break
        else:
            print(f"{count}OUT!!")
            count += 1