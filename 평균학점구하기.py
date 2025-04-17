## 1.어떤 학생의 성적 데이터 (학생,성적데이터,과목명,숫자, 알파벳)
## 2.txt 저장
## 3.txt 불러오기
## 4.평균 평점 구하기
## 5.txt 추가 저장

import random
import os
import ast


### 랜덤으로 과목 점수 만들기
def randScore ():
    return random.randint(80,100)

def randCredit ():
    return random.randint(2,3)

##과목명,학점,점수,등급 랜덤으로 만들기
def makeGrade ():
    totalCredit = 0
    sub = 1
    arr = []

    while totalCredit < 140:
        subject = "과목"+str(sub)
        sub += 1

        credit = randCredit()
        totalCredit += credit

        score = randScore()
        grade = ''
        if score >= 95:
            grade = 'A+'
        elif score >= 90:
            grade = 'A'
        elif score >= 85:
            grade = 'B+'
        elif score >= 80:
            grade = 'B'
        elif score >= 75:
            grade = 'C+'
        elif score >= 70:
            grade = 'C'
        else:
            grade = 'F'

        arr.append([subject,credit,score,grade])
    return arr


def saveFile (allScore):

    with open("과목 별 학점", 'a', encoding='utf-8') as f:

        for i in allScore:
            f.write(f"{i}\n")

##저장된 text 가져와 배열로 저장
def avgScore ():
    arr = []
    grade_to_point = {'A+': 4.5, 'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'F': 0.0}

    with open("과목 별 학점","r", encoding='utf-8') as f:
        lines = f.readlines()
        for i in lines:
            arr.append(ast.literal_eval(i.strip()))

    total_point = 0
    total_credit = 0

    for subject in arr:
        credit = subject[1]
        grade = subject[3]

        point = grade_to_point[grade]

        total_point += point * credit
        total_credit += credit

    avg_gpa = total_point / total_credit
    print(f"\n총 이수 학점: {total_credit}")
    print(f"평균 학점 (GPA): {avg_gpa:.2f}")
