#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201837 이름 : 박승민

import os
import time

# Q.1 10점
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

#함수정의
def solution(my_string, target):
    # my_string과 target을 매개변수로 하는 함수 solution 정의

    if 1 <= len(my_string) <= 100 and 1 <= len(target) <= 100:
    #제한사항을 if문으로 만들어
    #my_string과 target의 길이가 1보다 크거나 같고 100보다 작거나 같게 만들어줌

        if target in my_string:
        # 만약 target이 my_string 안에 포함되어 있다면 anser을 1로 초기화
            answer = 1

            return answer
            #answer값으로 return
        else: #그렇지않으면 answer을 0으로 초기화
            answer = 0

            return answer
            #answer값으로 return

my_string=input("my_string값을 입력해주세요: ")
target=input("target값을 입력해주세요: ")
answer = solution(my_string,target)
print(answer)


#my_string값과 target값을 input으로 사용자로부터 값을 받아 초기화
#solution 함수를 호출해서 answer를 선언하고 초기화 해준다
#answer값을 출력

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter): #letter을 매개변수로하는 solution함수 정의
    morse = {
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    #딕셔너리를 이용해서 모스부호를 알파벳으로 매핑한다

    morse_code = letter.split(' ')
    #매개변수를 통해 들어온 letter을 ' '(띄어쓰기)를 기준으로 분리 해서 morse_code에 저장한다

    answer = ''.join(morse[code]for code in morse_code)
    #answer값을 morse_code안에 있는 분리된 letter의 모스부호들을 매핑된 알파벳으로 바꿔주고
    #join을 통해 중간에 공백없이 합쳐준다

    return answer
    #answer값으로 return

letter = ".. -.-. .- -. - .... .. ... .- .-.. .-.. -.. .- -.--"
answer = solution(letter)
print(answer)

#letter을 내가 생각났던 명대사였던 캡틴아메리카 명대사가 나오도록 letter에 저장
#함수를 호출해서 answer값에 저장
#answer값을 출력

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age): #age를 매개변수를 하는 solution 함수 정의
    trans_age = { #trans_age라는 숫자를 알파벳으로 바꾸는 딕셔너리로 매핑
        '0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e',
        '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'
    }

    if 0 < age <= 1000: #제한사항
        str_age = str(age) #age를  str로 문자열로 바꿔 str_age에 저장

        answer = ''.join(trans_age[alphabet] for alphabet in str_age)
       #answer값을 str_age 모스부호들을 매핑된 알파벳으로 바꿔주고 join을 통해 모든 값들을 공백없이 합쳐서 저장

        return answer
        #answer값으로 return

#age값을 input으로 입력받고 나중에 있을 제한 사항의 비교 때문에 int로 바꿔주었다
#solution 함수를 호출해서 answer에 저장하고 print를 통해 출력한다.

age = input("행성의 나이를 입력하시오: ")
age = int(age)
answer = solution(age)
print(answer)

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

import math #표준라이브러리 모듈 중에 math 모듈을 가져옴

def solution(r1, r2): #r1,r2를 매개변수를 하는 solution함수 정의
    if  (1 <= r1 < r2 <= 1000000): #제한사항


      answer = 0 #answer를 0으로 초기화

    for x in range(-r2, r2 + 1): #x의 범위를 -r2부터 r2+1까지 for문으로 반복
        for y in range(-r2, r2 + 1):#y의 범위를 -r2부터 r2+1까지 for문으로 반복

            distance = math.sqrt(x**2 + y**2)
             #distance를 원들의 중심은 원점이니
             # 원점부터 점의 거리가 작은원의 반지름보다 크고 큰원 반지름보다 작은 점이 만약 있따면 answer에 1씩 더해준다
            if r1 <= distance <= r2:
                answer += 1

    return answer
    #answer값으로 return

r1 = input("r1을 입력하시오: ")
r1 = (int)(r1)
r2 = input("r2을 입력하시오: ")
r2 = (int)(r2)
answer = solution(r1, r2)
print(answer)

#r1의 값이랑 r2의 값을 input으로 받아주고 둘을 int형식으로 바꿔준다
#solution함수를 호출해서 answer값에 저장 하고 print로 answer값을 출력해준다.

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers): #numbers를 매개변수로 하는 solution함수 정의
    numbers = list(map(str, numbers))

    def compare(x, y): #x와 y를 매개변수로 하는 compare함수 정의
        if 0 > int(x + y) - int(y + x): #먄악 x와 y의 순서를 다르게해서 뺐을 때 음수면 1 양수면 0을 출력한다.
          return 1
        elif  0 < int(x + y) - int(y + x) :
          return 0

    for i in range(len(numbers) - 1): #i를 numbers-1의 길이만큼 반복
        for j in range(i + 1, len(numbers)):#범위가 i+1부터 numbers까지만큼 반복

            if compare(numbers[i], numbers[j]) == 1: #만약 numbers[i],numbers[j]를  compare했을때 결과가 1이면
                numbers[i], numbers[j] = numbers[j], numbers[i]  #numbers[j]와 number[i]의 순서를 바꿔서 저장

            # elif compare(numbers[i], numbers[j]) == 0:
            #     numbers[i], numbers[j] = numbers[i], numbers[j]
            # 0이면 바꿀필요가 없으니 생략

    answer = ''.join(numbers) #join으로 공백없이 numbers를 합쳐서 answer에 저장
    return str(answer) #제한사항 문자열로 바꾸기 위해 str을 사용해서 answer값 return

numbers = [8, 30, 17, 2, 23]
answer =solution(numbers)
print(answer)
#numbers 배열 선언하고
#answer에 solution함수를 변수를 numbers로 하여 호출하고 print로 출력