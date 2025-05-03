import tkinter as tk
from tkinter import messagebox

class BowlingGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.frames = [] # 투구 결과 저장
        self.scores = [] # 누적 점수 저장
        self.final_score = 0 # 최종 점수

    # 프레임 추가 및 점수 갱신
    def add_frame(self, frame):
        self.frames.append(frame)
        self.update_score()

    # 누적 점수 계산
    def update_score(self):
        self.scores = []
        total = 0
        for i in range(len(self.frames)):
            frame = self.frames[i]
            if i == 9: # 10프레임 특별 처리
                total += sum(frame)
                self.scores.append(total)
                continue
            if frame[0] == 10: # 스트라이크
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
            elif sum(frame[:2]) == 10: # 스페어
                bonus = 0
                if i + 1 < len(self.frames):
                    bonus += self.frames[i + 1][0]
                total += 10 + bonus
            else: # 일반
                total += sum(frame[:2])
            self.scores.append(total)
        self.final_score = self.scores[-1] if self.scores else 0

class BowlingApp:

    # GUI 초기화 및 구성
    def __init__(self, gui):
        self.gui = gui
        self.gui.title("볼링 게임")
        self.game = BowlingGame("플레이어1")
        self.frame_num = 1

        self.top_frame = tk.Frame(gui)
        self.top_frame.pack(side="top", fill="x", pady=10) # pady=10 -> 10픽셀만큼 상단 여백처리

        self.label = tk.Label(self.top_frame, text="1프레임 - 첫 번째 투구 점수를 선택하세요:")
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

        self.bottom_frame = tk.Frame(gui)
        self.bottom_frame.pack(side="bottom", fill="both", expand=True)
        # fill = "both" -> 부모 컨테이너 안에서 가로세로 모두 늘려줌

        self.result_text = tk.Text(self.bottom_frame, height=15, width=40)
        self.result_text.pack(fill="both", expand=True, pady=10)

        self.create_first_buttons()

    # 첫 투구 점수 선택 버튼 생성
    def create_first_buttons(self):
        for widget in self.first_frame.winfo_children():
            widget.destroy()
        self.first_score = None

        def make_handler(score):
            #자기 점수만 가지기 위해 사용
            def handler():
                self.select_first(score)

            return handler

        for i in range(0, 11):
            b = tk.Button(self.first_frame, text=str(i), width=3, command=make_handler(i))
            b.pack(side="left", padx=2)

    # 첫 투구 점수 선택 처리
    def select_first(self, score):
        self.first_score = score
        self.second_score = None
        self.third_score = None
        if self.frame_num < 10 and self.first_score == 10: # 스트라이크면 바로 다음 프레임
            self.second_score = 0
            self.second_label.pack_forget()
            self.second_frame.pack_forget()
            self.third_label.pack_forget()
            self.third_frame.pack_forget()
            self.gui.after(300, self.next_frame)
        else:
            self.second_label.pack()
            self.second_frame.pack()
            self.create_second_buttons()
            self.third_label.pack_forget()
            self.third_frame.pack_forget()

    # 두 번째 투구 점수 선택 버튼 생성
    def create_second_buttons(self):
        for widget in self.second_frame.winfo_children():
            widget.destroy()
        if self.frame_num == 10 and self.first_score == 10:
            max_score = 10
        else:
            max_score = 10 - self.first_score

        def make_handler(score):
            # 자기 점수만 가지기 위해 사용
            def handler():
                self.select_second(score)

            return handler

        for i in range(0, max_score + 1):
            b = tk.Button(self.second_frame, text=str(i), width=3, command=make_handler(i))
            b.pack(side="left", padx=2)

    # 두 번째 투구 점수 선택 처리
    def select_second(self, score):
        self.second_score = score
        if self.frame_num < 10:
            self.gui.after(300, self.next_frame)
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

    # 세 번째 투구 점수 선택 버튼 생성 (10프레임 한정)
    def create_third_buttons(self):
        for widget in self.third_frame.winfo_children():
            widget.destroy()
        if self.frame_num == 10:
            max_score = 10
        else:
            max_score = 10

        def make_handler(score):
            # 자기 점수만 가지기 위해 사용
            def handler():
                self.select_third(score)

            return handler

        for i in range(0, max_score + 1):
            b = tk.Button(self.third_frame, text=str(i), width=3, command=make_handler(i))
            b.pack(side="left", padx=2)

    # 세 번째 투구 점수 선택 처리 (10프레임 한정)
    def select_third(self, score):
        self.third_score = score
        self.gui.after(300, self.next_frame)

    # 프레임 결과 저장 및 다음 프레임 준비
    def next_frame(self):
        if self.frame_num < 10:
            frame = [self.first_score, self.second_score]
        else:
            frame = [self.first_score, self.second_score, self.third_score]
        self.game.add_frame(frame)
        self.show_total()
        self.frame_num += 1

        if self.frame_num > 10: # 게임 종료
            messagebox.showinfo("게임 종료", f"최종 점수: {self.game.final_score}")
            self.label.config(text="게임 종료!")
            self.first_frame.pack_forget()
            self.second_label.pack_forget()
            self.second_frame.pack_forget()
            self.third_label.pack_forget()
            self.third_frame.pack_forget()
        else:
            self.label.config(text=f"{self.frame_num}프레임 - 첫 번째 투구 점수를 선택하세요:")
            self.create_first_buttons()
            self.second_label.pack_forget()
            self.second_frame.pack_forget()
            self.third_label.pack_forget()
            self.third_frame.pack_forget()

    # 최종 점수 갱신
    def show_total(self):
        # 텍스트 박스 첫째줄 첫번째 내용 지우기
        self.result_text.delete(1.0, tk.END)
        # 각 프레임별 점수 출력
        for i in range(len(self.game.frames)):
            frame = self.game.frames[i]
            score = self.game.scores[i]
            text = "Frame {}: {} | 누적 점수: {}\n".format(i + 1, frame, score)
            self.result_text.insert(tk.END, text)

        # 최종 점수 출력
        self.result_text.insert(tk.END, "\n최종 점수: {}\n".format(self.game.final_score))

gui = tk.Tk()
app = BowlingApp(gui)
gui.mainloop()
