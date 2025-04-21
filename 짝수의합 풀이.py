#짝수의합 풀이
num = int(input("10000이하의 숫자를 입력하시오!"))
sum = 0

for i in range(1,num+1):
    sum += i if i % 2 == 0 else 0

print(f"{num} 이하 모든 짝수의 합: {sum}")

