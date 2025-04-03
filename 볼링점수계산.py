import random

def roll(): return random.randint(0, 10)

def generate_frames():
    frames = [(roll(), roll()) if (f < 9 and (r := roll()) < 10) else (10, 0) for f in range(9)]
    frames.append((roll(), roll(), roll() if sum(frames[-1][:2]) >= 10 else 0))
    return frames

def calculate_score(frames):
    score = 0
    for i, (f1, f2, *f3) in enumerate(frames):
        score += f1 + f2 + (f3[0] if f3 else 0)
        if i < 9 and f1 == 10:
            score += sum(frames[i+1][:2] if frames[i+1][0] < 10 else frames[i+1][:1] + frames[i+2][:1])
        elif i < 9 and f1 + f2 == 10:
            score += frames[i+1][0]
    return score

frames = generate_frames()
print("\n".join(f"Frame {i+1}: {f}" for i, f in enumerate(frames)))
print(f"Total Score: {calculate_score(frames)}")
