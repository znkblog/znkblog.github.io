---
title: "leetcode: 1. Two Sum"
description: "주어진 nums 배열에서, 합이 target이 되는 두 원소를 찾아 그 인덱스를 리턴하는 문제"
updated: "2026-10-20"
tags: ["leetcode", "array", "brute_force", "hash_table"]
---

## 문제

[https://leetcode.com/problems/two-sum](https://leetcode.com/problems/two-sum)

주어진 `nums` 배열에서, 합이 `target`이 되는 두 원소를 찾아 그 인덱스를 리턴하는 문제로, 동일한 원소를 두번 더하지 않으며, 합이 `target`되는 케이스가 반드시 오직 하나 존재한다.

## 완전 탐색(Brute Force)
```python
# 런타임 1831 ms, 메모리 19.8 MB
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, x in enumerate(nums[:-1]):
            for j, y in enumerate(nums[i+1:], i+1):
                if x + y == target:
                    return i, j
```

이중 루프로 전체 원소 쌍 케이스를 하나하나 탐색하는 [완전 탐색](/post/coding-test-basic#완전-탐색brute-force) 방식이다.

전체 원소 쌍 케이스를 만들 때, 외부 루프 `i`는 제일 마지막 원소를 탐색할 필요가 없고, 내부 루프 `j`는 `i`보다 앞선 인덱스를 탐색할 필요 없다.

문제에서 반드시 답이 하나 존재한다고 했으므로, 합이 `target`이 되는 원소를 찾으면 바로 인덱스를 리턴하고 종료한다.

## 해시 테이블(Hash Table)
```python
# 런타임 1 ms, 메모리 20.4 MB
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}

        for i, x in enumerate(nums):
            y = target - x
            if y in h:
                return h[y], i

            h[x] = i
```

[해시 테이블](/post/coding-test-basic#해시-테이블hash-table) 역할의 `h` 딕셔너리 생성하였다. `{ 원소값: 인덱스, ... }` 형태로 데이터 저장한다.

`i` 인덱스 순회에서 그 원소인 `x`와의 합이 `target`이 되는 원소가 저장소에 있는지를 검사, 있다면 인덱스 쌍을 리턴하고, 없다면 나중 순회를 위해 현재 순회의 원소값과 인덱스를 `h`에 저장해 둔다.

일반적으로 해시 테이블 자체의 원소 탐색 시간복잡도는 O(1)로 본다. 따라서 전체 코드의 순회가 한번(시간복잡도 O(N))이기 때문에 완전 탐색(시간복잡도 O(N²))보다 실행 속도가 빠르다.