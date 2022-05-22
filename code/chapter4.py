#주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def is_odd(number):
    if number%2 == 0:
        return '짝수'
    else:
        return '홀수'
print(is_odd(3))

#output= 홀수

#입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

def data(*args):
    sum=0
    for i in args:
        sum += i
    return sum/len(args)

print(data(1,2,3,4))

#output= 2.5

#다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다. 오류고치기

input1= int(input('첫번째숫자입력')) # <- int 를 넣어주지않으면, str 로 인식..?
input2= int(input('두번째숫자입력'))

total= input1 + input2

print("두수의합은 %s 입니다" %total)

#output= (input 이 3,6) 9

#출력결과는?
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

#================내정답
youneedpython
youneedpython
you,need,python #<- ',' 에는 공백삽입되어 저장된다
youneedpython

#output==============
youneedpython
youneedpython
you need python
youneedpython

#다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
#이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.
f1 = open("test.txt", 'w')
f1.write("Life is too short")

f2 = open("test.txt", 'r')
print(f2.read())
#===============================내 정답
f1= open("test.txt", 'w')
f1.write("Life is too short")
f1.close()  #<- 객체닫아주고, 다시열어야한다

f2= open("test.txt",'r')
fr= f2.read() #<- 정답에는 print(f2.read())
f2.close()
print(fr)

#output= Life is too short
