---
title: "leetcode: 912. Sort an Array"
description: "nums 배열의 숫자들을 오름차순으로 정렬하여 리턴하는 문제"
updated: "2026-10-xx"
tags: ["leetcode", "array", "divide_and_conquer", "heap", "sorting"]
---

## 문제
- [https://leetcode.com/problems/sort-an-array](https://leetcode.com/problems/sort-an-array)
- nums 배열의 숫자들을 오름차순으로 정렬하여 리턴하는 문제
- 추가로 언어가 자체 제공하는 정렬함수를 사용하지 말고, 시간복잡도 O(N log N)으로 풀 것도 요구하고 있음
- 아래 풀이보다 더 자세한 설명은 [정렬 알고리즘](https://namu.wiki/w/%EC%A0%95%EB%A0%AC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98) 참고 바람

## 버블 정렬(Bubble Sort)
```python
# 제한사항으로 실패
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(0, len(nums)-1):

            swapped = False
            for j in range(0, len(nums)-1-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True

            if not swapped:
                break

        return nums
```
- 아래와 같은 방식으로 정렬 수행
> - 0 인덱스 원소와 1 인덱스 원소를 비교, 0 인덱스 원소값 > 1 인덱스 원소값이라면 스왑
> - 1 인덱스 원소와 2 인덱스 원소를 비교, 1 인덱스 원소값 > 2 인덱스 원소값이라면 스왑
> - ...
> - N-2 인덱스 원소와 N-1 인덱스 원소를 비교, N-2 인덱스 원소값 > N-1 인덱스 원소값이라면 스왑
> - 이 결과 `nums` 안에서 가장 큰 값이 제일 N-1 인덱스(제일 마지막 자리)에 위치함
> - 다시 처음부터 N-2 인덱스 까지 동일한 비교를 반복, 이 결과 두번째로 큰 값이 N-2 번째에 위치함
> - 다시 처음부터 N-3 인덱스 까지 동일한 비교를 반복, 이 결과 세번째로 큰 값이 N-3 번째에 위치함
> - ...
- 이중 루프로 구현되어 있어 시간복잡도 O(N²)으로 풀리지는 않음, 동일한 값끼리 위치가 바뀌지 않기 때문에 안정 정렬
- `swapped` 변수로 중간에 스왑이 일어났는지를 파악함, 내부루프 반복 과정에서 스왑이 한번도 안일어났다면 이미 정렬이 되어 있는 상태라고 볼 수 있으므로 그 즉시 종료

## 선택 정렬(Selection Sort)
```python
# 제한사항으로 실패
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(0, len(nums)-1):

            minidx = i
            for j in range(i+1, len(nums)):
                if nums[minidx] > nums[j]:
                    minidx = j
            nums[i], nums[minidx] = nums[minidx], nums[i]

        return nums
```
- 아래와 같은 방식으로 정렬 수행
> - 0 ~ N-1 인덱스 중 가장 작은 원소값을 찾음, 0 인덱스 원소값과 가장 작은 원소값 스왑
> - 1 ~ N-1 인덱스 중 가장 작은 원소값을 찾음, 1 인덱스 원소값과 가장 작은 원소값 스왑
> - 2 ~ N-1 인덱스 중 가장 작은 원소값을 찾음, 2 인덱스 원소값과 가장 작은 원소값 스왑
> - ...
> - N-2 ~ N-1 인덱스 중 가장 작은 원소값을 찾음, N-2 인덱스 원소값과 가장 작은 원소값 스왑
> - 매 반복마다 앞에서부터 가장 작은 원소값들이 채워지게 됨
- 이중 루프로 구현되어 있어 시간복잡도 O(N²)으로 풀리지는 않음, 동일한 값끼리 위치가 바뀔 수 있기 때문에 불안정 정렬
- 