---
title: "투 포인터와 슬라이딩 윈도우"
description: "배열에서 두 원소 또는 특정 구간을 찾을 때, 이중 루프를 사용하는 대신 포인터 2개 지정하여 문제를 해결하는 방법"
updated: "2026-10-19"
tags: ["알고리즘", "배열", "투포인터", "슬라이딩윈도우"]
---

## 투 포인터와 슬라이딩 윈도우
- 어떤 배열에서 특정 조건을 만족하는 두 원소나 특정 구간을 찾을 때, 모든 케이스를 확인하는 이중 반복문을 떠올리기 쉬움
- 그러나 특정 조건을 만족하는 범위를 설정하고, 범위를 조정하는 것만으로 문제를 해결할 수 있는 경우가 있음
- 이 방식이 투 포인터로 **인덱스를 가리키는 포인터 두 개를 두고, 조건에 따라 포인터 하나씩 이동시키며 탐색**하는 방식임
- 크게 아래와 같이 두가지 종류로 나눌 수 있음

> - 양끝 포인터: 배열의 양 끝단에서 시작하여 범위를 좁혀나가는 투 포인터
> - 동방향 포인터: 두 포인터가 같은 방향으로 진행하며 범위를 조절해가는 투 포인터

- **동방향 포인터의 경우 슬라이딩 윈도우라고도 함**, 또한 두개 포인터 사용 대신 포인터 하나와 + 윈도우 크기로 나타낼 수도 있음

<!--adsense-->

## leetcode: 283. Move Zeroes
### 문제
- [https://leetcode.com/problems/move-zeroes](https://leetcode.com/problems/move-zeroes)
- 주어진 `nums` 배열을 in-place로 조작하여, 0을 모두 뒷쪽으로, 다른 숫자를 앞쪽으로 보내는 문제

### 완전 탐색(Brute Force)
- 반복문으로 순회하다가 0 값을 가진 원소를 찾으면, 다시 그 다음 원소부터 순회를 하여 0 아닌 값과 치환하는 풀이

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)-1):
            if nums[i] == 0:
                for j in range(i+1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
```

- 외부 루프 `i`는 0 을 찾아 순회, 0 원소를 찾았다면 내부 루프가 `i+1`부터 순회하여 0 이 아닌 값을 찾아 치환

### 슬라이딩 윈도우
- 포인터 + 윈도우 크기로 범위를 가리키는 슬라이딩 윈도우 구현, 한번의 순회로 문제 해결 가능
- 위 완전탐색보다 실행 속도가 빠름

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        size = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                size += 1
            else:
                nums[i-size], nums[i] = nums[i], nums[i-size]
```

- `i`로 순회하면서, 0 원소를 만나면 `size`를 하나씩 증가, 아니라면 `nums[i]`와 `nums[i-size]`를 치환
- 위와 같이 설정하면, 0 원소가 하나라도 있다면 `i-size`는 0 원소를 가리키게 되며, 치환으로 0 원소와 0이 아닌 원소 위치가 바뀌게 됨