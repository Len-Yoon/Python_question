import tkinter as tk
from tkinter import messagebox, simpledialog

class BowlingGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.frames = []
        self.scores = []
        self.final_score = 0

    def add_frame(self, frame):
        self.frames.append(frame)
        self.update_score()

    def update_score(self):
        self.scores = []
        total = 0
        for i in range(len(self.frames)):
            frame = self.frames[i]
            if i == 9:
                total += sum(frame)
                self.scores.append(total)
                continue
            if frame[0] == 10:
                bonus = 0
                if i + 1 < len(self.frames):
                    next_frame = self.frames[i + 1]
                    if next_frame[0] == 10:
                        bonus += 10
                        if i + 2 < len(self.frames):
                            bonus += self.frames[i + 2][0]
                        elif len(next_frame) > 1:
                            bonus += next_frame[1]
                    else:
                        bonus += next_frame[0] + next_frame[1]
                total += 10 + bonus
            elif sum(frame[:2]) == 10:
                bonus = 0
                if i + 1 < len(self.frames):
                    bonus += self.frames[i + 1][0]
                total += 10 + bonus
            else:
                total += sum(frame[:2])
            self.scores.append(total)
        self.final_score = self.scores[-1] if self.scores else 0

class Player:
    def __init__(self, name):
        self.game = BowlingGame(name)
        self.name = name

class PlayerCount(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="플레이어 수를 선택하세요 (1~4):").pack(padx=10, pady=10)
        self.var = tk.IntVar(value=1)
        self.spin = tk.Spinbox(master, from_=1, to=4, textvariable=self.var, width=5)
        self.spin.pack(pady=5)
        return self.spin

    def apply(self):
        self.result = self.var.get()

class BowlingApp:
    def __init__(self, gui, num_players):
        self.gui = gui
        self.gui.title("멀티 볼링 게임")

        self.players = [Player(f"플레이어 {i+1}") for i in range(num_players)]
        self.current_player_idx = 0
        self.frame_num = 1

        # 좌측 게임 패널
        self.left_frame = tk.Frame(gui)
        self.left_frame.pack(side="left", fill="both", expand=True)

        # 우측 점수 패널
        self.score_frame = tk.Frame(gui, width=200)
        self.score_frame.pack(side="right", fill="y", padx=10)
        self.player_labels = []
        for p in self.players:
            label = tk.Label(self.score_frame, text=f"{p.name}: 0", anchor="w")
            label.pack(fill="x", pady=2)
            self.player_labels.append(label)

        # 게임 컨트롤 요소
        self.top_frame = tk.Frame(self.left_frame)
        self.top_frame.pack(side="top", fill="x", pady=10)

        self.label = tk.Label(self.top_frame, text="")
        self.label.pack()

        self.first_frame = tk.Frame(self.top_frame)
        self.first_frame.pack()
        self.first_score = None
        self.second_score = None
        self.third_score = None

        self.second_label = tk.Label(self.top_frame, text="두 번째 투구 점수를 선택하세요:")
        self.second_frame = tk.Frame(self.top_frame)

        self.third_label = tk.Label(self.top_frame, text="세 번째 투구 점수를 선택하세요:")
        self.third_frame = tk.Frame(self.top_frame)

        self.bottom_frame = tk.Frame(self.left_frame)
        self.bottom_frame.pack(side="bottom", fill="both", expand=True)

        self.result_text = tk.Text(self.bottom_frame, height=15, width=50)
        self.result_text.pack(fill="both", expand=True, pady=10)

        self.update_turn_display()
        self.create_first_buttons()

    def update_turn_display(self):
        current_player = self.players[self.current_player_idx]
        self.label.config(
            text=f"{current_player.name} - {self.frame_num}프레임\n첫 번째 투구 점수를 선택하세요:"
        )
        self.update_scores()

    def update_scores(self):
        for idx, player in enumerate(self.players):
            score = player.game.final_score
            self.player_labels[idx].config(
                text=f"{player.name} | 점수: {score}",
                bg="lightblue" if idx == self.current_player_idx else "white"
            )

    def create_first_buttons(self):
        # winfo_children() -> 자식 객체 반환
        for widget in self.first_frame.winfo_children():
            widget.destroy()
        self.first_score = None

        def make_handler(score):
            def handler():
                self.select_first(score)
            return handler

        for i in range(0, 11):
            b = tk.Button(self.first_frame, text=str(i), width=3, command=make_handler(i))
            b.pack(side="left", padx=2)

    def select_first(self, score):
        self.first_score = score
        self.second_score = None
        self.third_score = None
        if self.frame_num < 10 and self.first_score == 10:
            self.second_score = 0
            self.second_label.pack_forget()
            self.second_frame.pack_forget()
            self.third_label.pack_forget()
            self.third_frame.pack_forget()
            self.next_frame()
        else:
            self.second_label.pack()
            self.second_frame.pack()
            self.create_second_buttons()
            self.third_label.pack_forget()
            self.third_frame.pack_forget()

    def create_second_buttons(self):
        # winfo_children() -> 자식 객체 반환
        for widget in self.second_frame.winfo_children():
            widget.destroy()
        if self.frame_num == 10 and self.first_score == 10:
            max_score = 10
        else:
            max_score = 10 - self.first_score

        def make_handler(score):
            def handler():
                self.select_second(score)
            return handler

        for i in range(0, max_score + 1):
            b = tk.Button(self.second_frame, text=str(i), width=3, command=make_handler(i))
            b.pack(side="left", padx=2)

    def select_second(self, score):
        self.second_score = score
        if self.frame_num < 10:
            self.next_frame()
        else:
            if (self.first_score == 10) or (self.first_score + self.second_score == 10):
                self.third_label.pack()
                self.third_frame.pack()
                self.create_third_buttons()
            else:
                self.third_label.pack_forget()
                self.third_frame.pack_forget()
                self.third_score = 0
                self.gui.after(300, self.next_frame)

    def create_third_buttons(self):
        # winfo_children() -> 자식 객체 반환
        for widget in self.third_frame.winfo_children():
            widget.destroy()
        max_score = 10

        def make_handler(score):
            def handler():
                self.select_third(score)
            return handler

        for i in range(0, max_score + 1):
            b = tk.Button(self.third_frame, text=str(i), width=3, command=make_handler(i))
            b.pack(side="left", padx=2)

    def select_third(self, score):
        self.third_score = score
        self.next_frame()

    def next_frame(self):
        player = self.players[self.current_player_idx]
        if self.frame_num < 10:
            frame = [self.first_score, self.second_score]
        else:
            frame = [self.first_score, self.second_score, self.third_score]
        player.game.add_frame(frame)
        self.show_total()

        # 다음 플레이어로 이동
        if self.current_player_idx < len(self.players) - 1:
            self.current_player_idx += 1
        else:
            self.current_player_idx = 0
            self.frame_num += 1

        # 게임 종료 체크
        if self.frame_num > 10:
            self.end_game()
        else:
            self.update_turn_display()
            self.create_first_buttons()
            self.second_label.pack_forget()
            self.second_frame.pack_forget()
            self.third_label.pack_forget()
            self.third_frame.pack_forget()

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
    root = tk.Tk()
    root.withdraw()  # 메인 윈도우 숨김
    dlg = PlayerCount(root, title="플레이어 수 선택")
    num_players = dlg.result if dlg.result else 1
    root.destroy()

    # 이제 메인 윈도우를 다시 생성하고 게임 시작
    gui = tk.Tk()
    app = BowlingApp(gui, num_players)
    gui.mainloop()
