import random


##자동 숫자 생성 (0점 부터 100점)
def ranNum():
    num = random.randint(50, 100)
    return num


## 4depth Dictionary (학년/반/학생/과목
def makeGradeScore():
    grade = {}

    for k in range(1, 7):
        ban = {}
        grade[str(k) + "학년"] = ban

        for j in range(1, 6):
            student = {}
            ban[str(j) + "반"] = student

            for i in range(1, 11):
                score = {}

                score["math"] = ranNum()
                score["eng"] = ranNum()
                score["kor"] = ranNum()

                student["학생" + str(i)] = score

    return grade


def GradeClassAvgScore(grade, a, b):
    math1 = 0
    eng1 = 0
    kor1 = 0

    for i in range(1, len(grade[f"{str(a)}학년"][str(b) + "반"]) + 1):
        math1 += grade[str(a) + "학년"][str(b) + "반"]["학생" + str(i)]["math"]
        eng1 += grade[str(a) + "학년"][str(b) + "반"]["학생" + str(i)]["eng"]
        kor1 += grade[str(a) + "학년"][str(b) + "반"]["학생" + str(i)]["kor"]

    print(f"{str(a)}학년 {str(b)}반 수학평균", math1 / 10)
    print(f"{str(a)}학년 {str(b)}반 영어평균", eng1 / 10)
    print(f"{str(a)}학년 {str(b)}반 국어평균", kor1 / 10)


def GradeAvgScore(grade, a):
    math2 = 0
    eng2 = 0
    kor2 = 0

    for i in range(1, len(grade[f"{str(a)}학년"]) + 1):
        for j in range(1, len(grade[f"{str(a)}학년"][str(i) + "반"]) + 1):
            math2 += grade[f"{a}학년"][str(i) + "반"]["학생" + str(j)]["math"]
            eng2 += grade[f"{a}학년"][str(i) + "반"]["학생" + str(j)]["eng"]
            kor2 += grade[f"{a}학년"][str(i) + "반"]["학생" + str(j)]["kor"]

    print(f"{a}학년 수학평균", math2 / 50)
    print(f"{a}학년 영어평균", eng2 / 50)
    print(f"{a}학년 국어평균", kor2 / 50)


## 전학년 학생 점수 랜덤으로 만들기
schoolScore = makeGradeScore()

#원하는 학년 반 세과목 평균
grade_num = input("평균을 알고싶은 학년과 반을 숫자로만 입력하세요 (띄어쓰기로 구분) ")

a,b = map(int,grade_num.split())

GradeClassAvgScore(schoolScore,a,b)

##원하는 학년 전 과목 평균
grade_num =  input("평균을 알고싶은 학년을 입력하세요")
GradeAvgScore(schoolScore,grade_num)