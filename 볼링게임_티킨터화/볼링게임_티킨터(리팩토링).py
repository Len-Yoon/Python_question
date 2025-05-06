import tkinter as tk
from tkinter import messagebox, simpledialog

# 볼링 게임 한 명의 점수와 프레임을 관리하는 클래스
class BowlingGame:
    def __init__(self, player_name):
        self.player_name = player_name  # 플레이어 이름 저장
        self.frames = []                # 각 프레임의 투구 점수(리스트) 저장
        self.scores = []                # 각 프레임까지의 누적 점수 저장
        self.final_score = 0            # 최종 점수

    # 새 프레임의 점수를 추가하고 누적 점수를 갱신
    def add_frame(self, frame):
        self.frames.append(frame)
        self.update_score()

    # 볼링 점수 규칙에 따라 누적 점수를 계산
    def update_score(self):
        self.scores = []
        total = 0
        for i in range(len(self.frames)):
            frame = self.frames[i]
            if i == 9:
                # 10번째 프레임은 보너스 투구까지 모두 합산
                total += sum(frame)
                self.scores.append(total)
                continue
            if frame[0] == 10:
                # 스트라이크: 다음 두 투구 점수를 보너스로 더함
                bonus = 0
                if i + 1 < len(self.frames):
                    next_frame = self.frames[i + 1]
                    if next_frame[0] == 10:
                        # 연속 스트라이크일 경우
                        bonus += 10
                        # 다다음 프레임 존재 확인
                        if i + 2 < len(self.frames):
                            bonus += self.frames[i + 2][0]
                        # 다다음 프레임 점수 추가
                        elif len(next_frame) > 1:
                            bonus += next_frame[1]
                    else:
                        bonus += next_frame[0] + next_frame[1]
                total += 10 + bonus
            elif sum(frame[:2]) == 10:
                # 스페어: 다음 한 투구 점수를 보너스로 더함
                bonus = 0
                # 다음 프레임 존재 확인
                if i + 1 < len(self.frames):
                    bonus += self.frames[i + 1][0]
                total += 10 + bonus
            else:
                # 일반 프레임: 두 투구의 합만 더함
                total += sum(frame[:2])
            self.scores.append(total)
        self.final_score = self.scores[-1] if self.scores else 0

# 각 플레이어별로 BowlingGame 인스턴스를 보유하는 클래스
class Player:
    def __init__(self, name):
        self.game = BowlingGame(name)
        self.name = name

# 플레이어 수를 입력받는 다이얼로그 팝업 창
class PlayerCount(simpledialog.Dialog):
    def body(self, master):
        # 팝업 창 크기 조정
        self.geometry("400x200")
        # 안내문과 Spinbox(1~4) 배치
        tk.Label(master, text="플레이어 수를 선택하세요 (1~4):").pack(padx=10, pady=10)
        self.var = tk.IntVar(value=1)
        self.spin = tk.Spinbox(master, from_=1, to=4, textvariable=self.var, width=10)
        self.spin.pack(pady=5)
        return self.spin  # 포커스를 줄 위젯 반환

    def apply(self):
        # 선택된 플레이어 수를 self.result에 저장
        # tk.intVar로 생성된 변수 저장
        self.result = self.var.get()

# 전체 게임 진행과 티킨터 GUI를 관리하는 클래스
class BowlingApp:
    def __init__(self, gui, num_players):
        self.gui = gui
        self.gui.title("멀티 볼링 게임")

        # 플레이어 인스턴스 생성
        self.players = [Player(f"플레이어 {i+1}") for i in range(num_players)]
        self.current_player_idx = 0  # 현재 플레이어 인덱스
        self.frame_num = 1           # 현재 프레임(1~10)

        # 좌측: 게임 진행 패널
        self.left_frame = tk.Frame(gui)
        self.left_frame.pack(side="left", fill="both", expand=True)

        # 우측: 점수판 패널 (플레이어별 점수 표시)
        self.score_frame = tk.Frame(gui, width=200)
        self.score_frame.pack(side="right", fill="y", padx=10)
        self.player_labels = []
        for p in self.players:
            label = tk.Label(self.score_frame, text=f"{p.name}: 0", anchor="w") # anchor="w" 텍스트 왼쪽 정렬
            label.pack(fill="x", pady=2)
            self.player_labels.append(label)

        # 상단: 턴 안내 및 점수 입력 버튼 영역
        self.top_frame = tk.Frame(self.left_frame)
        self.top_frame.pack(side="top", fill="x", pady=10)

        self.label = tk.Label(self.top_frame, text="")  # 현재 턴 안내 라벨
        self.label.pack()

        # 첫 번째/두 번째/세 번째 투구 버튼 영역 및 안내 라벨
        self.first_frame = tk.Frame(self.top_frame)
        self.first_frame.pack()
        self.first_score = None
        self.second_score = None
        self.third_score = None

        self.second_label = tk.Label(self.top_frame, text="두 번째 투구 점수를 선택하세요:")
        self.second_frame = tk.Frame(self.top_frame)

        self.third_label = tk.Label(self.top_frame, text="세 번째 투구 점수를 선택하세요:")
        self.third_frame = tk.Frame(self.top_frame)

        # 하단: 프레임별 점수 표시 텍스트 영역
        self.bottom_frame = tk.Frame(self.left_frame)
        self.bottom_frame.pack(side="bottom", fill="both", expand=True)

        self.result_text = tk.Text(self.bottom_frame, height=15, width=50)
        self.result_text.pack(fill="both", expand=True, pady=10)

        # 첫 턴 안내 및 첫 번째 투구 버튼 생성
        self.update_turn_display()
        self.create_first_buttons()

    # 현재 턴(플레이어, 프레임) 안내 및 점수판 업데이트
    def update_turn_display(self):
        current_player = self.players[self.current_player_idx]
        self.label.config(
            text=f"{current_player.name} - {self.frame_num}프레임\n첫 번째 투구 점수를 선택하세요:"
        )
        self.update_scores()

    # 플레이어별 점수판 갱신
    def update_scores(self):
        for idx, player in enumerate(self.players):
            score = player.game.final_score
            # 현재 플레이어는 배경색 강조
            self.player_labels[idx].config(
                text=f"{player.name} | 점수: {score}",
                bg="lightblue" if idx == self.current_player_idx else "white"
            )

    # 점수 선택 버튼을 동적으로 생성하는 함수
    def create_score_buttons(self, frame_widget, max_score, select_callback):
        # 기존 버튼 제거
        for widget in frame_widget.winfo_children():
            widget.destroy()

        # 각 점수별 버튼 생성
        def make_handler(score):
            def handler():
                select_callback(score)
            return handler

        for i in range(0, max_score + 1):
            b = tk.Button(frame_widget, text=str(i), width=3, command=make_handler(i))
            b.pack(side="left", padx=2)

    # 첫 번째 투구 점수 선택 버튼 생성
    def create_first_buttons(self):
        self.first_score = None
        self.create_score_buttons(self.first_frame, 10, self.select_first)

    # 첫 번째 투구 점수 선택 시 호출
    def select_first(self, score):
        self.first_score = score
        self.second_score = None
        self.third_score = None
        # 10프레임이 아니고 스트라이크면 두 번째 투구 없이 바로 다음 프레임
        if self.frame_num < 10 and self.first_score == 10:
            self.second_score = 0
            self.second_label.pack_forget()
            self.second_frame.pack_forget()
            self.third_label.pack_forget()
            self.third_frame.pack_forget()
            self.next_frame()
        else:
            # 두 번째 투구 안내 및 버튼 생성
            self.second_label.pack()
            self.second_frame.pack()
            self.create_second_buttons()
            self.third_label.pack_forget()
            self.third_frame.pack_forget()

    # 두 번째 투구 점수 선택 버튼 생성
    def create_second_buttons(self):
        # 10프레임에서 첫 투구가 스트라이크면 두 번째 투구도 0~10 가능
        if self.frame_num == 10 and self.first_score == 10:
            max_score = 10
        else:
            max_score = 10 - self.first_score  # 첫 투구와 합이 10 넘지 않도록 제한
        self.create_score_buttons(self.second_frame, max_score, self.select_second)

    # 두 번째 투구 점수 선택 시 호출
    def select_second(self, score):
        self.second_score = score
        if self.frame_num < 10:
            self.next_frame()
        else:
            # 10프레임에서 스트라이크/스페어면 세 번째 투구 가능
            if (self.first_score == 10) or (self.first_score + self.second_score == 10):
                self.third_label.pack()
                self.third_frame.pack()
                self.create_third_buttons()
            else:
                self.third_label.pack_forget()
                self.third_frame.pack_forget()
                self.third_score = 0
                self.gui.after(300, self.next_frame)

    # 세 번째 투구 점수 선택 버튼 생성 (10프레임 보너스)
    def create_third_buttons(self):
        self.create_score_buttons(self.third_frame, 10, self.select_third)

    # 세 번째 투구 점수 선택 시 호출
    def select_third(self, score):
        self.third_score = score
        self.next_frame()

    # 프레임 종료 후 다음 프레임/플레이어로 진행
    def next_frame(self):
        player = self.players[self.current_player_idx]
        # 10프레임이면 세 투구, 그 외엔 두 투구
        if self.frame_num < 10:
            frame = [self.first_score, self.second_score]
        else:
            frame = [self.first_score, self.second_score, self.third_score]
        player.game.add_frame(frame)
        self.show_total()  # 프레임별 점수 표시

        # 다음 플레이어로 이동
        if self.current_player_idx < len(self.players) - 1:
            self.current_player_idx += 1
        else:
            self.current_player_idx = 0
            self.frame_num += 1

        # 10프레임 모두 끝나면 게임 종료
        if self.frame_num > 10:
            self.end_game()
        else:
            self.update_turn_display()
            self.create_first_buttons()
            self.second_label.pack_forget()
            self.second_frame.pack_forget()
            self.third_label.pack_forget()
            self.third_frame.pack_forget()

    # 게임 종료 시 최종 점수 및 우승자 안내
    def end_game(self):
        winner = max(self.players, key=lambda p: p.game.final_score)
        msg = "\n".join([f"{p.name}: {p.game.final_score}" for p in self.players])
        messagebox.showinfo("게임 종료", f"최종 점수\n{msg}\n\n우승자: {winner.name}")
        self.label.config(text="게임 종료!")
        self.first_frame.pack_forget()
        self.second_label.pack_forget()
        self.second_frame.pack_forget()
        self.third_label.pack_forget()
        self.third_frame.pack_forget()

    # 각 플레이어의 프레임별 점수 및 누적 점수 표시
    def show_total(self):
        self.result_text.delete(1.0, tk.END)
        for idx, p in enumerate(self.players):
            self.result_text.insert(tk.END, f"{p.name} 프레임별 점수:\n")
            for i in range(len(p.game.frames)):
                frame = p.game.frames[i]
                score = p.game.scores[i]
                text = "  Frame {}: {} | 누적 점수: {}\n".format(i + 1, frame, score)
                self.result_text.insert(tk.END, text)
            self.result_text.insert(tk.END, f"  최종 점수: {p.game.final_score}\n\n")

if __name__ == "__main__":
    # 첫 실행 시 플레이어 수 입력 다이얼로그 표시
    root = tk.Tk()
    root.withdraw()  # 메인 윈도우 숨김
    dlg = PlayerCount(root, title="플레이어 수 선택")
    num_players = dlg.result if dlg.result else 1
    root.destroy()

    # 메인 윈도우 생성 후 게임 시작
    gui = tk.Tk()
    app = BowlingApp(gui, num_players)
    gui.mainloop()
