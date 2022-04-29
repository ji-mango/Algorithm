'''
'산업 스파이의 편지'
문제 : 안녕하세요. 저는 산업 스파이입니다. 저의 정체를 절대 다른 사람에게 말하지 말아주세요.
저의 가장 최근 일은 유명한 수학 연구소의 최신 연구 결과를 훔쳐오는 것이었습니다. 저는 매우 유능한 산업 스파이이기 때문에, 연구 결과를 어렵지 않게 얻을 수 있었습니다. 
하지만, 제가 올 것을 미리 알았는지 연구소에서는 연구 결과를 모두 서류 절단기에 넣어버렸습니다. 어쩔수 없이 저는 눈물을 머금고 종이 조각을 모두 훔쳐왔습니다.
저를 고용한 사람은 매우 무서운 사람입니다. 또, 저는 프로이기 때문에 실수를 용납하지 않습니다. 어떻게든 이 종이를 모두 복구해가야합니다. 
이 연구소의 연구 주제는 빠른 소인수 분해입니다. 제가 가진 종이 조각에는 숫자가 한 자리씩만 적혀져 있습니다. 원래 숫자가 뭐였는지를 잘 모르겠습니다. 
종이 조각에 쓰여 있는 숫자를 보내드릴테니, 종이 조각을 적절히 배치해서 소수가 되는 경우가 몇 개이지 알려주실 수 있나요?
감사합니다.

스파이 드림.

입력 : 첫째 줄에 테스트 케이스의 개수 c가 주어진다. (1 ≤ c ≤ 200) 각 테스트 케이스는 한 줄로 이루어져 있고, 종이조각에 쓰여 있는 수가 공백없이 주어진다. 
종이조각의 수는 적어도 1개, 많아야 7개이다.

출력 : 각 테스트 케이스에 대해 종이조각을 적절히 배치해서 만들 수 있는 서로 다른 소수의 개수를 출력한다. 이때, 모든 종이 조각을 사용하지 않아도 된다. 
(7과 1이 있을 때, 만들 수 있는 소수는 7, 17, 71이다) 종이 조각을 적절히 배치해서 만든 숫자가 0으로 시작할 때, 앞에있는 0을 지운 수가 같으면 같은 숫자이다.

풀이 : 1. 에라스토테네스의 체를 통해, 9999999까지의 소수 여부를 판별(종이조각 수가 최대 7개이고 가장 큰 숫자가 9이므로 소수 판별 최댓값은 9999999로 설정)
      2. 종이조각을 배치해서 만들 수 있는 수를 순열을 통해 구한 후 (1)에서 만든 배열을 통해 소수인지 알아낸 후 소수일 경우 result += 1
         * 종이조각을 배치해서 만든 숫자가 0으로 시작할 때, 0을 지운 수가 같으면 같은 숫자라고 했으므로 숫자가 0으로 시작하면 해당 숫자는 무시한다.

comment : 저번에 에라스토테네스의 체 관련 문제를 푼 적이 있어서 수월하게 풀 수 있었다.
'''
from itertools import permutations
import math

num = 9999999                               # 종이조각 수가 최대 7개이고 가장 큰 숫자가 9이므로 소수 판별 최댓값은 9999999로 설정
prime = [True for i in range(num+1)]        # 해당 숫자(인덱스)가 소수라면 True, 소수가 아니라면 False를 넣을 배열

for i in range(2, int(math.sqrt(num)+1)):   # 에라스토테네스의 체
    if prime[i]:
        j = 2
        while i*j <= num:
            prime[i*j] = False
            j+=1
prime[1] = False                            # 1은 소수가 아니므로

c = int(input())
for i in range(c):
    result = 0
    temp = input()
    lenT = len(temp)
    num = []
    for j in range(lenT):                   # 입력받은 숫자를 각각 int형으로 배열에 넣어줌
        num.append(int(temp[j]))
    for j in range(1, lenT+1):
        per = list(set(permutations(num, j)))
        for x in per:                       # 각 순열을 숫자로 만듦      
            p = ''
            for y in x:
                p += str(y)
            if p and p[0] != '0':           # p값이 없거나 맨앞자리가 0일 경우는 제외
                p = int(p)
                if prime[p]:
                    result += 1
    print(result)