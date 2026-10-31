---
title: "leetcode: 704. Binary Search"
description: "정수 원소로 이뤄져있으며 오름차순으로 정렬된 nums 배열에서 target을 찾아 인덱스를 리턴하는 문제"
updated: "2026-11-xx"
tags: ["leetcode", "array", "binary_search"]
---


## 문제
[https://leetcode.com/problems/binary-search](https://leetcode.com/problems/binary-search)

정수 원소로 이뤄져있으며 오름차순으로 정렬된 `nums` 배열에서 `target`을 찾아 인덱스를 리턴하는 문제다. (`target`이 없다면 -1을 리턴)

또한 시간복잡도가 O(log N)이 되도록 알고리즘을 구현하도록 요구하고 있다.

## 이진 탐색(Binary Search)
```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i, j = 0, len(nums)

        while i < j:
            m = i + (j - i) // 2

            if nums[m] < target:
                i = m + 1
            else:
                j = m

        return i if i < len(nums) and nums[i] == target else -1
```

초기값으로 `nums` 범위 전체를 `i`이상 `j`미만이 되도록 가리킨다.

while 반복문으로 중간값 `nums[m]`를 계산하고 `target`과 비교해서 `i` 또는 `j`를 조정한다. 범위를 ~이상 ~미만으로 정했기 때문에 `i`와 `j`의 조정 수식이 다르다.

코드를 위와 같이 구성하면 어떠한 경우든 반복문의 결과는 항상 `i == j`가 된다. 이 때의 `i`(또는 `j`)는 `nums` 안에서 `target`이 오름차순을 유지한 채 들어갈 수 있는 인덱스를 가리키게 된다.

