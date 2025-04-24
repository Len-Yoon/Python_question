import os
import random

# 플레이어 클래스
class Player:
    def __init__(self, name):
        self.name = name
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def average_score(self):
        return sum(game.final_score for game in self.games) / len(self.games)


# 볼링 게임 클래스
class Game:
    def __init__(self, player_name, game_number):
        self.player_name = player_name
        self.game_number = game_number
        self.frames = []
        self.scores = []
        self.final_score = 0

    def roll(self):
        return random.randint(5, 10)

    def second_roll(self, remain_score):
        return random.randint(0, remain_score)

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
        self.final_score = self.scores[-1]

    # 점수 누적 계산
    def update_score(self):
        total = 0
        self.scores = []
         # *f3 사용이유: 나머지 항목을 리스트로 모아주는 역할
        for i in range(len(self.frames)):
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
    def print_save(self):
        filename = f"{self.player_name}의 볼링 점수표.txt"
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"{self.player_name}의 {self.game_number}번째 게임 볼링 점수표\n")
            print(f"\n{self.player_name}의 {self.game_number}번째 게임\n")

            for i, frame in enumerate(self.frames):
                line = f"Frame {i+1}: {frame} | Current Score: {self.scores[i]}"
                print(line)
                f.write(line + "\n")

            print(f"\nFinal Total Score: {self.final_score}\n")
            f.write(f"\nFinal Total Score: {self.final_score}\n\n")

# 전체 경기 관리 클래스
class Bowling:
    def __init__(self, names):
        self.players = [Player(name) for name in names]
        self.game_players = len(names)

    def run(self):
        for player in self.players[:random.randint(1, len(self.players))]:  # 랜덤 인원 선택
            for game_num in range(1, self.game_players + 1):
                game = Game(player.name, game_num)
                game.play_game()
                game.print_save()
                player.add_game(game)

        self.print_avg()

    def print_avg(self):
        print("\n 인원별 평균 점수 요약 ")
        for player in self.players:
            if player.games:
                print(f"{player.name}의 평균 점수: {player.average_score():.1f}")


# main 함수

names = ["홍길동", "이순신", "김두한", "유관순", "이완용"]
a = Bowling(names)
a.run()
