import os
import random

# 플레이어 이름 리스트
names = ["홍길동", "이순신", "김두한", "유관순", "이완용"]

# 볼링 게임 클래스
class Game:
    def __init__(self, player_name, game_number):
        self.player_name = player_name      # 플레이어 이름
        self.game_number = game_number      # 몇 번째 게임인지
        self.frames = []                    # 10프레임까지의 기록 저장
        self.scores = []                    # 각 프레임별 누적 점수 저장

    def roll(self):
        return random.randint(5, 10)

    def second_roll(self, remaining):
        return random.randint(0, remaining)

    # 전체 게임 플레이 (10프레임)
    def play_game(self):
        for i in range(10):
            if i == 9:  # 마지막 프레임
                f1 = self.roll()
                f2 = 0 if f1 == 10 else self.second_roll(10 - f1)
                f3 = self.roll()
                frame = [f1, f2, f3]
            else:
                f1 = self.roll()
                f2 = 0 if f1 == 10 else self.second_roll(10 - f1)
                frame = [f1, f2]
            self.frames.append(frame)
            self.update_score()

    # 점수 누적 계산
    def update_score(self):
        total = 0
        self.scores = []
        for i in range(len(self.frames)):
            # *f3 사용이유: 나머지 항목을 리스트로 모아주는 역할
            f1, f2, *f3 = self.frames[i]
            total += f1 + f2 + (f3[0] if f3 else 0)

            # 스트라이크 보너스
            if i < 8 and f1 == 10:
                next_two = [0, 0]
                if i + 1 < len(self.frames):
                    if self.frames[i + 1][0] == 10 and i + 2 < len(self.frames):
                        next_two = [self.frames[i+1][0], self.frames[i+2][0]]
                    else:
                        next_two = self.frames[i+1][:2]
                total += sum(next_two)

            # 스페어 보너스
            elif i < 9 and f1 + f2 == 10:
                if i + 1 < len(self.frames):
                    total += self.frames[i+1][0]

            self.scores.append(total)

    # 실시간 점수 출력 및 저장
    def print_and_save(self):
        filename = f"{self.player_name}의 볼링 점수표.txt"
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"{self.player_name}의 {self.game_number}번째 게임 볼링 점수표\n")
            print(f"\n{self.player_name}의 {self.game_number}번째 게임\n")

            for i, frame in enumerate(self.frames):
                line = f"Frame {i+1}: {frame} | Current Score: {self.scores[i]}"
                print(line)
                f.write(line + "\n")

            final_score = self.scores[-1]
            print(f"\nFinal Total Score: {final_score}\n")
            f.write(f"\nFinal Total Score: {final_score}\n\n")

        return self.scores[-1]  # 최종 점수 반환

# 랜덤 인원 수 결정
def man_num():
    return random.randint(1, len(names))


player_averages = {}

for i in range(man_num()):
    player = names[i]
    scores = []

    for game_num in range(1, 6):  # 각 플레이어는 5번 게임
        g = Game(player, game_num)
        g.play_game()
        final_score = g.print_and_save()  # 마지막 점수 받아오기
        scores.append(final_score)

    # 평균 점수 저장
    avg_score = sum(scores) / len(scores)
    player_averages[player] = avg_score

# ▶ 평균 점수 출력
print("\n 인원별 평균 점수 요약 ")
for player, avg in player_averages.items():
    print(f"{player}의 평균 점수: {avg:.1f}")
