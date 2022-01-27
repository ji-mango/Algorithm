'''
'떡볶이 떡 만들기'

문제 : 동빈이네 떡볶이 떡은 떡의 길이가 일정하지 않다. 대신 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가
될 것이다. 잘린 떡의 길이는 차례대로 4, 0, 0, 2cm 이다. 손님은 6cm 만큼의 길이를 가져간다.

comment : 이러한 문제가 전형적인 이진 탐색 문제라는 것을 알고 놀랐다. 아마 이진탐색을 공부하지 않았다면 못풀었을 것 같다.
처음에는 이 문제를 어떻게 이진탐색으로 풀어야 하는지 잘 감이 오지 않았는데, 풀고 나니까 이러한 문제들이 이진 탐색으로 풀어야
쉽게 풀 수 있다는 것을 깨달았다.
'''
N, M = map(int, input().split())
rice = list(map(int, input().split()))

result = 0
def binary_search(start, end):
    global result
    while start <= end:
        sum = 0
        mid = (start + end) // 2
        for i in rice:
            if mid < i:
                sum += i - mid
        if sum == M:
            result = mid
            return
        elif sum > M:
            result = mid
            start = mid + 1
        else:
            end = end - 1
    return

binary_search(0, max(rice))
print(result)

