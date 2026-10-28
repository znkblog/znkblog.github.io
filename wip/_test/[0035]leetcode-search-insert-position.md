---
title: "leetcode: 35. Search Insert Position"
description: "오름차순 정렬되어있는 nums 배열에서, target이 위치한 또는 target이 들어갈 수 있는 인덱스를 찾아 리턴하는 문제"
updated: "2026-10-20"
tags: ["leetcode", "array", "binary_search", "two_pointers"]
---

## 문제
- [https://leetcode.com/problems/search-insert-position](https://leetcode.com/problems/search-insert-position)
- 오름차순 정렬되어있는 `nums` 배열에서, `target`이 위치한 또는 `target`이 들어갈 수 있는 인덱스를 찾아 리턴하는 문제
- 반드시 시간복잡도 O(log N)으로 풀어야 함

## 이진 탐색(Binary Search)
```python
# 런타임 0 ms, 메모리 19.8 MS
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
- 배열이 오름차순으로 정렬되어 있다면 [이진 탐색](https://namu.wiki/w/%EC%9D%B4%EC%A7%84%20%ED%83%90%EC%83%89) 알고리즘을 적용할 수 있음
- 두개의 포인터 `i`, `j`는 각각 `nums`에서 `target`이 있을 가능성이 있는 범위의 하한, 상한을 가리며, `i` 이상, `j` 이하로 해석하면 됨
- while 반복문과 그 안 내용을 위와 같이 설정하면, 어떤 케이스라도 반드시 `i > j`가 되는 순간이 발생하며, 그 때의 `i`가 `target`이 있거나 또는 `target`이 오름차순 유지한 채 들어갈 수 있는 인덱스가 됨
- 참고로 while 반복문 안쪽 if 조건문에 `nums[m] == target`에 대한 별도 처리가 없음, 조건문을 보면 `j`를 조정하게 되는데, 만일 `target`이 7이고 `nums` 안에 7이 여러개 있다고 하면, while 반복문의 결과 `i`는 제일 왼쪽의 7 인덱스를 가리키게 되며, 반대로 `i` 조정으로 처리했다면, `i`는 가장 오른쪽 7 인덱스의 다음 인덱스를 가리키게 됨

## python 라이브러리
```python
# 런타임 0 ms, 메모리 19.9 MB
import bisect

class Solution:
    def searchInsert(self, nums: lsit[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
```
- python에서 이진 탐색용으로 제공하는 bisect 라이브러리 사용
- 앞선 코드의 `nums[m] == target`일 때 `i`를 조정하냐 `j`를 조정하냐에 따른 두가지 함수를 제공하며, 세부적인 사항은 [python 도움말](https://docs.python.org/ko/3/library/bisect.html) 참고