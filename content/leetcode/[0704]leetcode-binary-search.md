---
title: "leetcode: 704. Binary Search"
description: "정수 원소로 이뤄져있으며 오름차순으로 정렬된 nums 배열에서 target을 찾아 인덱스를 리턴하는 문제"
updated: "2026-11-02"
tags: ["leetcode", "array", "binary_search"]
---


## 문제
[https://leetcode.com/problems/binary-search](https://leetcode.com/problems/binary-search)

정수 원소로 이뤄져있으며 오름차순으로 정렬된 `nums` 배열에서 `target`을 찾아 인덱스를 리턴하는 문제입니다. (`target`이 없다면 -1을 리턴)

또한 시간복잡도가 O(log N)이 되도록 알고리즘을 구현하도록 요구하고 있습니다.


## 이진 탐색(Binary Search)
```python
# 런타임 1 ms, 메모리 20.38 MB
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

초기값으로 `nums` 범위 전체를 `[i, j)`, 즉 `i`이상 `j`미만이 되도록 가리킵니다.

while 반복문으로 중간값 `nums[m]`를 계산하고 `target`과 비교해서 `i` 또는 `j`를 조정합니다.

범위를 ~이상 ~미만으로 정했기 때문에 `nums[m] < target`이면 `i = m + 1`, 아니라면 `j = m` 식으로 조정 수식이 비대칭임을 확인할 수 있습니다.

코드를 위와 같이 구성하면 어떠한 경우든 반복문의 결과는 항상 `i == j`가 됩니다. 이때 `i`(또는 `j`)는 `nums` 안에서 `target`이 오름차순을 유지한 채 들어갈 수 있는 인덱스를 가리키게 됩니다.

참고할 점은 위 while 반복문에서는 `nums[m] == target`일 때 바로 리턴하지 않는다는 것입니다. if 조건식을 보면 `j`를 조정합니다. 아래의 예시로 이에 따른 결과를 예측해 보겠습니다.

```python
target = 7
nums = [2, 3, 5, 7, 7, 7, 7, 7, 7, 11, 13]
```

`target`과 동일한 값이 여러 개 존재합니다. 위에서 언급한 것처럼 while 반복문은 이 경우라도 마지막엔 `i == j`가 되어 종료하는데, 7이 있는 가장 앞 인덱스인 3을 가리킵니다.

만일 if 조건문을 `nums[m] <= target`으로 바꿨다면 어떻게 될까요? `nums[m] == target`인 경우 `i`를 조정하게 됩니다. 이렇게 바꿔도 while 반복문은 언젠가 `i == j`가 되어 종료되며, 이때는 7이 있는 가장 뒤 인덱스의 다음 인덱스인 9를 가리킵니다.

차이점을 확인할 수 있지만 본 문제를 풀 때는 어떤 부등호를 사용해도 문제를 풀 수 있습니다. 본 문제의 제약사항을 잘 읽어보면 모든 원소가 고유하다고 되어 있습니다. 즉 위 예시와 같이 `target`값이 여러 개 포함된 `nums`는 문제 케이스로 제공하지 않기 때문입니다.


## bisect 라이브러리 사용
```python
# 런타임 0 ms, 메모리 20.48 MB
import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i = bisect.bisect_left(nums, target)

        return -1 if i == len(nums) or nums[i] != target else i

```

python은 이진 탐색을 수행하는 라이브러리를 기본 제공합니다. 위 코드에서 임포트하고 있는 bisect 라이브러리가 그것이며 여기서 제공하는 bisect_left 함수로 문제를 풀 수 있습니다.

참고로 bisect_left 함수는 위 챕터 코드와 같이 `j`를 조정하는 (그래서 `target`이 여러개 있는 경우 가장 앞 인덱스를 가리키는) 로직과 동일하게 작동합니다.

`i`를 조정하는 것처럼 가장 뒤 인덱스를 가리키도록 작동하는 bisect_right(또는 bisect) 함수도 있습니다.

python 도움말의 [bisect](https://docs.python.org/ko/3/library/bisect.html) 문서를 참고하면 더 상세한 정보를 알 수 있습니다.