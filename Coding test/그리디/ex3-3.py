'''
'숫자 카드 게임'
문제 : 숫자 카드 게임은 여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장을
      뽑는 게임이다. 룰은 다음과 같다.
      1. 숫자가 쓰인 카드들이 N X M 형태로 놓여있다. 이때 N은 행의 개수이고,
      M은 열의 개수이다.
      2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
      3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
      4. 따라서 처음에 카드를 골라낸 행을 선택할 때, 이후에 해당 행에서 가장
      숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를
      뽑을 수 있는 전략을 세워야 한다.

      게임의 룰에 맞게 카드를 뽑는 프로그램을 만드시오.

배운 점 : 최댓값을 구할 때 굳이 maximum과 하나씩 비교할 필요없이 max함수를 사용하면 된다.
'''

N, M = map(int, input().split())
li=[]
for i in range(N):
    li.append(list(map(int,input().split())))

maximum = 0
for i in range(N):
    if min(li[i]) > maximum:
        maximum = min(li[i])
    # maximum=max(maximum,min(li[i]))도 가능!

print(maximum)