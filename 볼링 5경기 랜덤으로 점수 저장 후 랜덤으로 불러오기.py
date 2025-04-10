import os
import random
frames = []
name = ["홍길동","이순신","김두한","유관순","이완용"]

def man_num():
    return random.randint(1,len(name))

def roll():
    return random.randint(5,10);

def second_roll(num):
    return random.randint(0,num);

def generate_frames():

    for i in range(1,11):
        if i < 10:
            frame = [roll()]
            if frame[0] == 10:
                frame.append(0)
            else:
                frame.append(second_roll(10-frame[0]))
            frames.append(frame)
        else:
            frame = [roll()]
            if frame[0] == 10:
                frame.append(0)
            else:
                frame.append(second_roll(10-frame[0]))
            frame.append(roll())

            frames.append(frame)

def calculate_score(frames):
    score = 0
    for i, (f1, f2, *f3) in enumerate(frames):
        score += f1 + f2 + (f3[0] if f3 else 0)
        if i < 8 and f1 == 10:
            score += sum(frames[i+1][:2] if frames[i+1][0] < 10 else frames[i+1][:1] + frames[i+2][:1])
        elif i < 9 and f1 + f2 == 10:
            if i + 1 < len(frames):
                score += frames[i+1][0]
    return score


for i in range(man_num()):
    for j in range (1,6):
        frames = []
        generate_frames()
        with open(f"{name[i-1]}의 볼링 점수표",'a', encoding='utf-8') as f:
            f.write(f"{name[i-1]}의 {j}번 째 게임 볼링 점수표 \n")
            f.write("\n".join(f"Frame {i+1}: {f}" for i, f in enumerate(frames)))
            f.write(f"\nTotal Score: {calculate_score(frames)}\n")

