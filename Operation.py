'''
#연산자
#num1 =3
#num2 =4
#print(type(num1))
#print('덧셈: ',num1 + num2)
#print('뺄셈: ',num1 - num2)
#print('곱셈: ',num1 * num2)
#print('나머지: ',num2 % num1)

#res = num1 + num2
#print('res: ',res)
#res += num1
#print('res: ',res)
# ++, -- 지원X
#res += 1
#res = res + 1

#비교연산자
#참, 거짓 --> True, False
#print(num1 > num2)
#print(num1 == num2)
#print(num1 != num2)

#논리연산자
#print(num1 > num2 and num1 < num2)
#print(num1 > num2 or num1 < num2)
#print(not(num1 > num2))

# 3항 연산자    
result = (num1 > num2) and 'num1이 num2보다 크다' or 'num1이 num2보다 작다'
print(result)

#문자열

str1 = '이불'
str2 = '밖은 위험해'
fullStr = str1 + str2
print('문자열 연결: ', fullStr)
fullStr = fullStr + '\n' + '노는게 제일 좋아'
print('개행문자: ', fullStr)

#문자열 인덱싱(indexing)
print(fullStr[0], fullStr[1], fullStr[2])
'''
'''
#[]--> 리스트(list)
#문자열 자르기(slicing)

fullStr = '홍길동입니다.'
print(fullStr[0:2]) # 0 ~ 1까지
print(fullStr[1:]) # 1 ~ 끝까지
print(fullStr[:3]) # 처음부터 ~ 2까지
print(fullStr[1::2]) # 1 ~ 끝까지 2번째 위치만

#in 연산자
search = '길동' in fullStr
print(search)

length = len(fullStr)
print('변수값 크기: ', length)


#입력 처리
print('1번째 숫자 입력: ')
input1 = input()
print(type(input1))
input2 = input('2번째 숫자 입력: ')
print(input2)

# int() : 문자열 -> 숫자
# str() : 숫자 -> 문자열
sum = int(input1) + int(input2)
print('숫자 덧셈: ', sum)
input3 = int(input('3번째 숫자 입력: '))
print(type(input3))
'''
'''
#1.원주율 PI를 저장하는 변수 생성 PI=3.14
#2.원의 반지름 입력받기
#3.원의 면적 구하기(반지름X반지름XPI)
PI = 3.14
input3 = int(input('반지름 입력: '))
sum1 = float(input3) * float(input3) * float(PI)
print('면적: ',sm)


#온도(화씨 -> 섭씨) 구하는 프로그램
#1.화씨 온도 입력받기 (정수)
#2.섭씨온도 = (화씨온도 -32)/1.8
#3.섭씨온도 출력하기

input1 = int(input('화씨온도 입력: '))
sum2 = float((input1) - 32)/1.8
print('섭씨온도: ', sum2)


#총점과 평균 구하는 프로그램
#1.국어,영어,수학 점수 입력받기
#2.총점과 평균값 구하고 출력하기.

kr = int(input('국어 점수: '))
er = int(input('영어 점수: '))
sr = int(input('수학 점수: '))

add = kr + er + sr
re = float(add) / 3
print('총점: ',add)    #print('총점:{0}, 평균:{1}'.format(add, re))
print('평균: ',re)


#홀수, 짝수 판단 프로그램(3항 연산자)
#1.숫자 1개 입력
#2.홀짝 판단 하여 "홀수", "짝수" 출력하기

st = int(input('숫자 입력: '))
ae = (st %2 == 0 ) and '"짝수"' or '"홀수"'
print(ae)
'''

#동전교환기 프로그램
#1.동전은 각각 500원, 100원, 50원, 10원...
#2.특정 금액의 입력받기(ex: 1360)
#3.아래 출력형식으로 출력 

#----------------------------
#동전교환기 프로그램 v1.0
#----------------------------
#오백원 개수: 2개
#백원 개수: 3개
#50원 개수: 1개
#10원 개수: 1개
#----------------------------
print('-----------------------')

d = int(input('금액 입력: '))
a = d / 500
c = d % 500 / 100
b = d % 500 % 100 / 50
v = d % 500 % 100 % 50 / 10 

print('오백원 개수: %d개'%a)
print('백원 개수: %d개'%c)
print('50원 개수: %d개'%b)
print('10원 개수: %d개'%v)
print('-----------------------')