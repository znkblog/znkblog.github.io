---
title: "leetcode: 1. Two Sum"
description: "정수를 원소로 가진 nums 배열이 있을 때, 합이 target이 되는 원소 쌍을 리턴하는 문제"
updated: "2026-10-31"
tags: ["leetcode", "array", "brute_force", "hash_table", "two_pointers"]
---


## 문제
[https://leetcode.com/problems/two-sum](https://leetcode.com/problems/two-sum)

정수를 원소로 가진 `nums` 배열이 있을 때, 합이 `target`이 되는 원소 쌍을 리턴하는 문제다.

반드시 정답이 유일하게 존재한다.


## 완전 탐색(Brute Force)
```python
# 런타임 1714 ms, 메모리 19.52 MB
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
```

`nums` 배열로 만들 수 있는 모든 원소 쌍 전수를 탐색하는 [완전 탐색](https://namu.wiki/w/%EB%B8%8C%EB%A3%A8%ED%8A%B8%20%ED%8F%AC%EC%8A%A4) 방식이다.

이중 루프로 구현되어 있다. 외부 루프, 내부 루프 모두 `nums` 모든 원소를 순회할 필요는 없다. 위 코드처럼 루프를 구현해도 모든 원소 쌍을 탐색할 수 있다.


## 해시 테이블(Hash Table)
```python
# 런타임 0 ms, 메모리 20.28 MB
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ht = {}

        for i, x in enumerate(nums):
            y = target - x
            if y in ht:
                return ht[y], i
            else:
                ht[x] = i
```

`ht` 딕셔너리는 [해시 테이블](https://namu.wiki/w/%ED%95%B4%EC%8B%9C#s-4)로서 `{ 원소값: 인덱스, ... }` 형식의 데이터를 저장한다.

`nums`를 순회하면서, 순회하는 원소값 `x`의 상대값 `target - x`가 `ht`에 있는지를 검사, 있다면 리턴하고 없다면 다음 순회를 위해 저장해 둔다.


## 투 포인터(Two Pointers)
```python
# 런타임 9 ms, 메모리 21.96 MB
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums = sorted(
            [{"idx": i, "val": x} for i, x in enumerate(nums)], key=lambda x: x["val"]
        )

        i, j = 0, len(nums) - 1
        while i < j:
            total = nums[i]["val"] + nums[j]["val"]
            if total < target:
                i += 1
            elif target < total:
                j -= 1
            else:
                return nums[i]["idx"], nums[j]["idx"]
```

`nums`를 `{"idx": 인덱스, "val": 원소값}` 데이터를 가진 배열로 변환하고 오름차순으로 정렬을 한다.

`nums`의 하한과 상한 인덱스를 가리키는 `i`, `j` 투 포인터를 상정하고, while 반복문 안에서 포인터가 가리키는 원소 쌍의 합 `total`과 `target` 크기를 비교해 `i` 또는 `j`를 조정한다.