---
title: "[배열] 이진 탐색"
description: "오름차순으로 정렬된 배열에서 특정 원소를 찾아내는 가장 효율적인 방법"
updated: "2026-10-19"
tags: ["array", "binary_search"]
---

## 이진 탐색 알고리즘
- 배열이 있고, 그 안에서 원하는 값 `target`을 찾고자 할 때는, 보통 배열 제일 앞 원소부터 순차적으로 검색을 함, 그러나 이 방식은 운이 나쁘면 `target`을 찾는데 아주 오랜 시간이 걸릴 수 있음
- 엑셀을 많이 이용해본 사용자는 알겠지만, VLOOKUP 함수에 "정확히 일치" 옵션을 주고 사용하면, 범위에서 target을 순서대로 검사해가며 찾는데, 수식과 데이터양이 많아질수록 엑셀 계산 속도가 현저히 느려진 경험을 한번쯤은 해봤을 것임, 순차검색의 문제임
- 하지만 **배열이 오름차순으로 정렬이 되어있다면, 특별한 알고리즘으로 원하는 데이터를 빠르게 찾을 수 있음**, 이른바 이진 탐색인데 어떤 알고리즘인지는 [나무위키](https://namu.wiki/w/%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89) 링크 안의 그림만 봐도 쉽게 이해가 될 것임, 그리고 왜 배열이 사전에 오름차순으로 정렬이 되어있어야 하는지도 충분히 이해가 될 것이라 생각함
- `A` 배열에서 `target` 원소값을 찾고자 한다면, 대체로 아래와 같은 방식으로 찾으면 됨

> - A 전체 범위에서 중간위치값 middle을 찾아서, target과 비교
> - middle < target이면 middle 포함 그 아래 데이터들을 모두 버리고, target < middle이면 middle 포함 그 위 데이터들을 모두 버림
> - 버리지않고 남은 데이터들을 다시 A로 정의하고, 위 단계를 middle == target이 될 때까지 계속 반복

<!--adsense-->

## leetcode: 35. Search Insert Position
### 문제
- [https://leetcode.com/problems/search-insert-position](https://leetcode.com/problems/search-insert-position)
- 오름차순 정렬된 `nums` 배열에서 `target`이 위치한 인덱스 찾거나, `target`이 없다면 오름차순 유지한 채 삽입이 가능한 인덱스를 찾아 리턴하는 문제

### 이진 탐색 사용
- 알고리즘 원리는 간단한데 이를 코드로 옮기는게 생각보다 까다로움

```python
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i, j = 0, len(nums)-1

        while i <= j:
            m = i + (j-i)//2

            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1 

        return i
```
- `i`와 `j`는 이진 탐색 대상 범위를 좁혀가는 투 포인터임, `target`이 위치해있을 범위를 `i`이상 `j`이하로 정의
- 이렇게 세팅하고 while 반복문을 실행하면 어떠한 케이스든 `i > j`가 되는 시점이 반드시 나오게 되는데, 이 때의 `i`가 문제가 요구하는 리턴값임, 즉 `target`이 `nums` 안에 있었다면 그 인덱스가 되며, 없었다면 `target`이 들어갈만한 위치를 가리키는 인덱스가 됨
- 참고로 while 반복 중간에 `nums[m] == target`이 되었다고 바로 리턴하지 않도록 되어있음, 아래와 같이 `target`과 동일한 값이 여러개 있는 케이스로 이게 어떤 의미인지 생각해볼 수 있음

```python
target = 7
nums = [2, 3, 5, 7, 7, 7, 7, 7, 7, 11, 13]
```
- 코드는 `nums[m] == target`인 경우 `j`를 조정하도록 되어있음, 즉 `m`인덱스보다 뒤에 있는 원소들을 버리는 셈이 되는데, 위 케이스에서는 while 반복문 종료가 되었을 때 `i`는 원소 7들이 모여있는 구간의 제일 앞부분 인덱스인 3이 됨
- 만일 `i`를 조정하도록 했다면 결과는 원소 7들이 모여있는 구간의 제일 뒤쪽 다음 인덱스인 9가 됨

### 빌트인 라이브러리 사용
- Python은 이진 탐색을 지원하는 별도 빌트인 라이브러리가 있어, 이를 사용해서 문제를 풀 수도 있음

``` python
import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
```

- 동일한 값에 대한 처리를 어떻게 하느냐에 따라 크게 bisect_left, bisect_right 함수로 나뉨, 위에서 `i`를 조정하는 방식이 bisect_left와 같으며, `j`를 조정하는 방식이 bisect_right와 같음
- bisect 라이브러리 상세한 명세는 [python 도움말](https://docs.python.org/ko/dev/library/bisect.html)을 참고하기 바람

