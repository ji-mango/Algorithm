'''
'잃어버린 괄호'
문제 : 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

comment : 처음에 어디에 괄호를 쳐야할 지 모르겠어서 헤맸다.
'''
oper = input()
oper = oper.split('-')
array = []

for i in oper:
    temp = 0
    i = i.split('+')
    for j in i:
        temp += int(j)
    array.append(temp)

answer = array[0]
for i in range(1, len(array)):
    answer -= array[i]

print(answer)
