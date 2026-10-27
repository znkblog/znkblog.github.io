---
title: "완전 탐색, 투 포인터, 슬라이딩 윈도우"
description: "배열과 같은 연속된 데이터 자료구조에서 자주 사용되는 완전 탐색, 투 포인터, 슬라이딩 윈도우 알고리즘"
updated: "2026-10-26"
tags: ["알고리즘", "완전탐색", "슬라이딩윈도우", "투포인터", "algorithm", "brute_force", "sliding_window", "two_pointers"]
---

## 완전 탐색(Brute Force)
- 문제 해결을 위해 가능한 모든 케이스나 가짓수를 탐색하는 방법
- 모든 케이스를 탐색하므로 답을 반드시 찾을 수 있고 알고리즘 이해가 쉬우나, 최적화가 안되어 있어 실행 속도는 느린 편

## 투 포인터(Two Pointers)
- 배열같은 연속된 데이터 자료구조에서 **인덱스를 가리키는 두 개의 포인터를 두고 특정 조건을 만족할 때 포인터를 이동시켜 문제를 해결**하는 최적화 방식 중 하나
- 크게 아래와 같이 두 종류가 있음
> - 양 끝 포인터: 데이터 구간의 처음과 끝을 지정한 뒤, 구간을 좁히는 방향으로 포인터 이동
> - 동방향 포인터: 데이터 구간의 처음에 두 포인터를 지정한 뒤, 각각 조건에 따라 같은 방향으로 포인터 이동
- 두 포인터의 이동 조건을 정확하게 지정하여 불필요한 탐색을 줄이는 것이 포인트로, 주로 완전탐색이 이중 루프를 사용할 때의 시간복잡도 O(N²)을 O(N)으로 줄임

## 슬라이딩 윈도우(Sliding Window)
- 배열같은 연속된 데이터 자료구조에서 **특정 구간(윈도우)을 유지하면서 구간을 이동시켜가며 문제를 해결**하는 최적화 방식 중 하나
- 구간을 `시작점+끝점` 또는 `시작점+구간사이즈`와 같은 형태로 정의, 윈도우 크기를 고정하거나 변경해 가며 문제 해결
- 사실상 동방향 투 포인터와 동일한 개념으로 생각해도 됨
- 구간 이동 조건을 정확하게 지정하여 불필요한 탐색을 줄여야 하며, 특히 구간을 변경할 때 구간에서 빠지게되는 부분과 새로 추가되는 부분만으로 갱신하여 연산 횟수도 줄이는 것이 포인트, 이 역시 완전탐색이 이중 루프를 사용할 때의 시간복잡도를 O(N)으로 줄임

## leetcode: 283. Move Zeroes
### 문제
- [https://leetcode.com/problems/move-zeroes](https://leetcode.com/problems/move-zeroes)
- 주어진 `nums` 배열을 in-place로 조작하여, 0 원소를 모두 뒷쪽으로 다른 숫자를 앞쪽으로 보내는 문제

### 완전 탐색(Brute Force)
- 반복문으로 순회하다가 0 값을 가진 원소를 찾으면, 다시 그 다음 원소부터 순회를 하여 0 아닌 값과 치환
```python
# 런타임 1543 ms, 메모리 20.2 MB
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
- 외부 루프 `i`는 0 을 찾아 순회, 0 원소를 찾았다면 내부 루프가 `i+1`부터 순회하여 0이 아닌 값을 찾아 치환

### 투 포인터
- 두개의 포인터가 한번의 순회로 문제 해결하며, 완전 탐색보다 실행 속도가 빠름
```python
# 런타임 9 ms, 메모리 20.2 MB
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        for i in range(0, len(nums)):
            while z < i and not(nums[z] == 0):
                z += 1

            if z < i:
                nums[z], nums[i] = nums[i], nums[z]
```
- 투 포인터는 `z`와 `i` 상정, `z`는 현재 가장 앞에 있는 0 값을 가리키고, `i`는 `nums`를 차례대로 순회하는 포인터
- 매 순회마다 `z`는 `i`보다 작으면서, 값이 0인 원소를 찾아 인덱스를 가리키게 됨, 만일 0인 원소를 찾지 못한다면 로직 상 `z == i`가 됨
- `z < i`인 경우 `z`는 0 원소를 확실히 가리키고 있으므로 이 때 `z` 인덱스와 `i` 인덱스 값을 스왑
- 단일 루프로 구현되어 시간복잡도는 O(N)