import random

frames = []

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
        if i < 9 and f1 == 10:
            score += sum(frames[i+1][:2] if frames[i+1][0] < 10 else frames[i+1][:1] + frames[i+2][:1])
        elif i < 9 and f1 + f2 == 10:
            score += frames[i+1][0]
    return score


generate_frames()
print("\n".join(f"Frame {i+1}: {f}" for i, f in enumerate(frames)))
print(f"Total Score: {calculate_score(frames)}")


