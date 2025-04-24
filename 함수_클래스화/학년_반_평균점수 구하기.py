import random

##자동 숫자 생성 (0점 부터 100점)
def ranNum():
    num = random.randint(50,100)
    return num

## 4depth Dictionary (학년/반/학생/과목)
grade = {}
for k in range(1,7):
    ban = {}
    grade[str(k)+"학년"] = ban

    for j in range(1,6):
        student = {}
        ban[str(j)+"반"] = student

        for i in range(1,11):
            score = {}

            score["math"] = ranNum()
            score["eng"] = ranNum()
            score["kor"] = ranNum()

            student["학생" + str(i)] = score


##1학년 1반 세과목 평균
math1 = 0
eng1 = 0
kor1 = 0

for i in range(1,len(grade["1학년"]["1반"])+1):
    math1 += grade["1학년"]["1반"]["학생"+str(i)]["math"]
    eng1 += grade["1학년"]["1반"]["학생" + str(i)]["eng"]
    kor1 += grade["1학년"]["1반"]["학생" + str(i)]["kor"]

print("1학년 1반 수학평균",math1/10)
print("1학년 1반 영어평균",eng1/10)
print("1학년 1반 국어평균",kor1/10)



##1학년 전체 과목 평균
math2 = 0
eng2 = 0
kor2 = 0
for i in range(1,len(grade["1학년"])+1):
    for j in range(1,len(grade["1학년"][str(i)+"반"])+1):
        math2 += grade["1학년"][str(i)+"반"]["학생" + str(j)]["math"]
        eng2 += grade["1학년"][str(i)+"반"]["학생" + str(j)]["eng"]
        kor2 += grade["1학년"][str(i)+"반"]["학생" + str(j)]["kor"]

print("1학년 수학평균", math2/50)
print("1학년 영어평균", eng2/50)
print("1학년 국어평균", kor2/50)