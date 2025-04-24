import random


class make_Score:

    def __init__(self):
        self.grade = {}

    ##자동 숫자 생성 (0점 부터 100점)
    def ranNum(self):
        num = random.randint(50, 100)
        return num

    def makeGradeScore(self):

        for k in range(1, 7):
            ban = {}
            self.grade[str(k) + "학년"] = ban

            for j in range(1, 6):
                student = {}
                ban[str(j) + "반"] = student

                for i in range(1, 11):
                    score = {}

                    score["math"] = self.ranNum()
                    score["eng"] = self.ranNum()
                    score["kor"] = self.ranNum()

                    student["학생" + str(i)] = score

        return self.grade


class grade_class_avg_score:

    def __init__(self, grade, a, b):
        self.grade = grade
        self.a = a
        self.b = b

    def GradeClassAvgScore(self):
        math1 = 0
        eng1 = 0
        kor1 = 0

        for i in range(1, len(self.grade[f"{str(self.a)}학년"][str(self.b) + "반"]) + 1):
            math1 += self.grade[str(self.a) + "학년"][str(self.b) + "반"]["학생" + str(i)]["math"]
            eng1 += self.grade[str(self.a) + "학년"][str(self.b) + "반"]["학생" + str(i)]["eng"]
            kor1 += self.grade[str(self.a) + "학년"][str(self.b) + "반"]["학생" + str(i)]["kor"]

        print(f"{str(self.a)}학년 {str(self.b)}반 수학평균", math1 / 10)
        print(f"{str(self.a)}학년 {str(self.b)}반 영어평균", eng1 / 10)
        print(f"{str(self.a)}학년 {str(self.b)}반 국어평균", kor1 / 10)


class grade_avg_score:

    def __init__(self, grade, a):
        self.grade = grade
        self.a = a

    def GradeAvgScore(self):
        math2 = 0
        eng2 = 0
        kor2 = 0

        for i in range(1, len(self.grade[f"{str(self.a)}학년"]) + 1):
            for j in range(1, len(self.grade[f"{str(self.a)}학년"][str(i) + "반"]) + 1):
                math2 += self.grade[f"{self.a}학년"][str(i) + "반"]["학생" + str(j)]["math"]
                eng2 += self.grade[f"{self.a}학년"][str(i) + "반"]["학생" + str(j)]["eng"]
                kor2 += self.grade[f"{self.a}학년"][str(i) + "반"]["학생" + str(j)]["kor"]

        print(f"{self.a}학년 수학평균", math2 / 50)
        print(f"{self.a}학년 영어평균", eng2 / 50)
        print(f"{self.a}학년 국어평균", kor2 / 50)

## 전학년 학생 점수 랜덤으로 만들기
schoolScore = make_Score().makeGradeScore()

## 원하는 학년 반 세과목 평균
grade_num = input("평균을 알고싶은 학년과 반을 숫자로만 입력하세요 (띄어쓰기로 구분) ")
a,b = map(int,grade_num.split())

avg = grade_class_avg_score(schoolScore,a,b)
avg.GradeClassAvgScore()

## 원하는 전 학년 평균 구하기
grade_num =  input("평균을 알고싶은 학년을 입력하세요")
avg = grade_avg_score(schoolScore,grade_num)
avg.GradeAvgScore()