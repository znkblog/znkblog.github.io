---
title: "leetcode: 136. Single Number"
description: "nums 배열 안 원소들이 하나를 제외하고 모두 두번씩 있을 때, 하나만 존재하는 원소를 찾아내는 문제"
updated: "2026-10-24"
tags: ["leetcode", "array", "bit_manipulation", "math"]
---

## 문제
- [https://leetcode.com/problems/single-number](https://leetcode.com/problems/single-number)
- nums 배열 안 원소들이 하나를 제외하고 모두 두번씩 있을 때, 하나만 존재하는 원소를 찾아내는 문제

## 비트 조작
```python
# 런타임 2 ms, 메모리 21.3 MB
import functools

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return functools.reduce(xor, nums)
```
- xor [비트 연산](https://namu.wiki/w/%EB%B9%84%ED%8A%B8%20%EC%97%B0%EC%82%B0)의 특징을 활용함, 동일한 값의 xor 연산은 0이 되기 때문에 `nums`의 모든 원소 xor 연산의 결과는 오직 동일한 쌍이 없는 원소만 남게 됨

## 카운팅
```python
# 런타임 7 ms, 메모리 21.7 MB
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        h = {}
        for n in nums:
            h[n] = h.get(n, 0) + 1

        return min(h, key=lambda x: h[x])
```
- `nums`를 순회, 각 원소가 나온 횟수를 `h` 딕셔너리에 기록한 뒤, `h` 에서 밸류값이 가장 적은 키를 리턴

## python 라이브러리 사용
```python
# 런타임 7 ms, 메모리 21.7 MB
import collections

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return collections.Counter(nums).most_common()[-1][0]
```
- python collections 라이브러리에 있는 Counter 컬렉션을 사용, Counter의 상세한 내용은 [python 도움말](https://docs.python.org/ko/3/library/collections.html#collections.Counter) 참고

## 수학 공식 활용
```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return sum(set(nums))*2 - sum(nums)
```
- `nums` 안 원소들에서 고유한 것들만 합을 구해 2배를 한 다음 `nums` 전체 합을 차감해서 구하는 방법