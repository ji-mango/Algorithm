'''
'0 만들기'
문제 : 1부터 N까지의 수를 오름차순으로 쓴 수열 1 2 3 ... N을 생각하자.
그리고 '+'나 '-', 또는 ' '(공백)을 숫자 사이에 삽입하자(+는 더하기, -는 빼기, 공백은 숫자를 이어 붙이는 것을 뜻한다). 
이렇게 만든 수식의 값을 계산하고 그 결과가 0이 될 수 있는지를 살피자.
N이 주어졌을 때 수식의 결과가 0이 되는 모든 수식을 찾는 프로그램을 작성하라.

입력 : 첫 번째 줄에 테스트 케이스의 개수가 주어진다(<10).
각 테스트 케이스엔 자연수 N이 주어진다(3 <= N <= 9).

출력 : 각 테스트 케이스에 대해 ASCII 순서에 따라 결과가 0이 되는 모든 수식을 출력한다. 각 테스트 케이스의 결과는 한 줄을 띄워 구분한다.
'''
a = int(input())
array = []
for i in range(a):
    array.append(int(input()))

def dfs(n):
    global result
    global resultStr
    global b
    if n == b:
        if result == 0:
            endStr.append(resultStr)
        return
    for i in range(3):
        if i == 0:
            result = result + (n+1)
            resultStr += '+'+str(n+1)

            dfs(n+1)
            resultStr = resultStr[:-2]
            result = result - (n+1)
            
        elif i == 1:
            resultStr += ' '+str(n+1)
            temp = resultStr.replace(' ','')
            result = eval(temp)
            
            dfs(n+1)
            resultStr = resultStr[:-2]
            temp = resultStr.replace(' ','')
            result = eval(temp)
            
            
        else:
            resultStr += '-'+str(n+1)
            result = result - (n+1)
            
            dfs(n+1)
            resultStr = resultStr[:-2]
            result = result + (n+1)
            

for x in array:
    b = x
    result = 1
    resultStr = '1'
    endStr = []
    dfs(1)
    endStr = sorted(endStr)
    for y in endStr:
        print(y)
    print()