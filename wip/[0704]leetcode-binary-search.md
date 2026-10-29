---
title: "leetcode: 704. Binary Search"
description: "오름차순 정렬된 배열에서 target의 위치(인덱스)를 찾아 리턴하는 문제"
updated: "2026-10-24"
tags: ["leetcode", "array", "breadth_first_search", "matrix"]
---

## 문제
[https://leetcode.com/problems/binary-search](https://leetcode.com/problems/binary-search)

오름차순 정렬된 배열에서 `target`의 위치(인덱스)를 찾아 리턴하는 문제다. (`target`이 없다면 -1을 리턴)

추가로 시간복잡도 O(log N)으로 풀도록 요구하고 있다.

## 이진 탐색(Binary Search)
```python
# 런타임 0 ms, 메모리 20.3 MB
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i, j = 0, len(nums)

        while i < j:
            m = i + (j-i)//2
            if nums[m] < target:
                i = m + 1
            else:
                j = m

        return -1 if i == len(nums) or nums[i] != target else i
```

오름차순으로 정렬된 배열에서 `target`값을 찾을 때는 [이진 탐색](/post/coding-test#이진-탐색binary-search)를 사용할 수 있다.

범위를 나타내는 포인터를 `i`이상 `j`미만으로 정의하였다. ~이상 ~미만의 범위이기 때문에 위 코드 if 조건문의 `i`와 `j` 포언터의 조정이 다르다.

위와 같이 코드를 구현하면 어떠한 경우든 반드시 `i == j` 시점이 발생하고 while 반복문이 종료된다. 그리고 이 때의 `i` 또는 `j`는 `target`이 있는 인덱스를 가리킨다. 만일 그 인덱스에 `target`이 없다면 오름차순을 해치지 않으면서 `target`이 들어갈 수 있는 인덱스가 된다.

참고로 if 조건문을 보면 `nums[m] == target`을 처리하는 구문이 없다. 이는 `target`이 여러개 존재하는 배열에 대한 처리 때문인데, 예를들어 아래와 같은 `nums`와 `target`이 있다고 해보자.

```python
nums = [2, 3, 5, 7, 7, 7, 7, 7, 7, 11, 13]
target = 7
```

위 코드에선 `nums[m] == target`이 되면 `j`를 조정한다. (즉 위쪽 상한을 범위에서 버린다.) 예시를 가지고 추적해보면 알겠지만 while 반복문이 종료되면 `i` 또는 `j`는 제일 앞쪽의 7이 있는 인덱스인 3을 가리킨다. 만일 `j`가 아니라 `i`를 조정하도록 했다면 제일 뒤 7이 있는 인덱스의 다음 인덱스인 9를 가리킨다.

코드에서는 `i`가 `num` 범위를 벗어났거나, `nums[i]`가 `target`이 아니라면 문제에서 요구하는 -1을 리턴하고 아니라면 `target`이 위치한 인덱스인 `i`를 리턴한다.

## python 라이브러리 사용
```python

```





## 이진 탐색(Binary Search)
배열에서 어떤 값을 찾을 땐 순차로 탐색한다. 하지만 배열이 오름차순으로 정렬이 되어있다면 이진 탐색 알고리즘으로 원하는 데이터를 빠르게 찾을 수 있다.

배열 `A`에서 `target`을 찾는다고 하면 아래와 같은 방식을 사용하면 된다.
> - A 전체 범위에서 중간위치값 middle을 찾아서, target과 비교
> - middle < target이면 middle 포함 그 아래 데이터들을 모두 버리고, target < middle이면 middle 포함 그 위 데이터들을 모두 버림
> - 남아있는 범위의 데이터들을 다시 A로 정의하고, 범위가 빌 때까지 위 단계를 계속 반복

더 상세한 설명은 나무위키의 [이진 탐색](https://namu.wiki/w/%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89) 문서를 참고하자.