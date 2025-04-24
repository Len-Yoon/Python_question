import random
import ast

class GradeMaker:
    def __init__(self):
        self.subjects = []

    def rand_score(self):
        return random.randint(90, 100)

    def rand_credit(self):
        return random.randint(2, 3)

    def get_grade(self, score):
        if score >= 95:
            return 'A+'
        elif score >= 90:
            return 'A'
        elif score >= 85:
            return 'B+'
        elif score >= 80:
            return 'B'
        elif score >= 75:
            return 'C+'
        elif score >= 70:
            return 'C'
        else:
            return 'F'

    def make(self):
        total_credit = 0
        count = 1

        while total_credit < 140:
            name = f"과목{count}"
            count += 1
            credit = self.rand_credit()
            total_credit += credit
            score = self.rand_score()
            grade = self.get_grade(score)

            self.subjects.append([name, credit, score, grade])

        return self.subjects

    def save(self, grades):
        with open("과목 별 학점", 'w', encoding='utf-8') as f:
            for item in grades:
                f.write(f"{item}\n")

class GradeFile:
    def __init__(self):
        self.grade_to_point = {
            'A+': 4.5, 'A': 4.0, 'B+': 3.5,
            'B': 3.0, 'C+': 2.5, 'C': 2.0, 'F': 0.0
        }

    def load_and_avg(self):
        data = []
        with open("과목 별 학점", 'r', encoding='utf-8') as f:
            for line in f:
                data.append(ast.literal_eval(line.strip()))

        total_point = 0
        total_credit = 0

        for subject in data:
            credit = subject[1]
            grade = subject[3]
            point = self.grade_to_point.get(grade, 0)
            total_point += point * credit
            total_credit += credit

        avg = total_point / total_credit if total_credit else 0

        print(f"\n총 이수 학점: {total_credit}")
        print(f"평균 학점 (GPA): {avg:.2f}")

# 학점 및 등급 생성 후 저장
maker = GradeMaker()
grades = maker.make()  # 학점 데이터 생성
maker.save(grades)

# 파일 읽고 GPA 계산
file = GradeFile()
file.load_and_avg()