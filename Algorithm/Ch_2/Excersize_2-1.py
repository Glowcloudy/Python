# 학생 5명의 시험 점수를 입력받아 합계와 평균을 출력하기

print('학생 그룹 점수의 합계와 평균을 구합니다.')

# 학생 N명의 수를 입력 및 점수를 담을 make list/total initialize
students = int(input('학생 수를 입력하세요.:'))
scores=[]
total=0

# input scores N student
for i in range(students):
    score=int(input('성적을 입력하세요. :'))
    scores.append(score)
    total += score

# score1 = int(input('1번 학생의 점수를 입력하세요.: '))
# score2 = int(input('2번 학생의 점수를 입력하세요.: '))
# score3 = int(input('3번 학생의 점수를 입력하세요.: '))
# score4 = int(input('4번 학생의 점수를 입력하세요.: '))
# score5 = int(input('5번 학생의 점수를 입력하세요.: '))

# total =0

# total += score1
# total += score2
# total += score3
# total += score4
# total += score5

# print result
print(f'합계는 {total}점입니다.')
print(f'평균는 {total/5}점입니다.')