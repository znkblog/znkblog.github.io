---
title: "이진 탐색"
description: "오름차순으로 정렬된 데이터 집합에서 타겟 값을 빠르게 찾는 알고리즘"
updated: "2026-10-26"
tags: ["알고리즘", "이분탐색", "이진탐색"]
---

## 이진 탐색(Binary Search)
- 배열과 같은 데이터 집합에서 어떤 값 `target`을 찾고자 할 때는 보통 순회를 해야하므로 시간복잡도는 O(N)이 됨
- 그러나 데이터가 **오름차순(또는 내림차순)으로 정렬이 되어 있다면 이진 탐색(이분 탐색 이라고도 함) 알고리즘으로 빠른 탐색**이 가능하며, 시간복잡도는 O(log N)이 됨
- 배열이 오름차순으로 정렬되어 있을 때 `target`을 아래와 같은 방식으로 탐색
> - 배열의 중간 인덱스 m에 위치한 데이터 middle과 target을 비교
> - middle < target이라면 m보다 앞에 위치한 데이터들을 모두 버림 (m보다 앞에 위치한 데이터들도 모두 middle < target이기 때문)
> - target < middle이라면 m보다 뒤에 위치한 데이터들을 모두 버림 (m보다 뒤에 위치한 데이터들도 모두 target < middle이기 때문)
> - 버리고 남은 범위의 중간 인덱스 m에 위치한 데이터를 다시 middle로 삼고 target과 비교 반복

## leetcode: 35. Search Insert Position
### 문제
- [https://leetcode.com/problems/search-insert-position](https://leetcode.com/problems/search-insert-position)
- 오름차순 정렬되어있는 `nums` 배열에서, `target`이 위치한 또는 `target`이 들어갈 수 있는 인덱스를 찾아 리턴하는 문제로 시간복잡도 O(log N)으로 풀 것을 요구

### 반복문으로 이진 탐색
- 앞서 언급한 알고리즘을 코드화, `target`을 찾았다고 바로 리턴하지 않음 (동일값 처리 방식에 유념해 볼 것)
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
- `i`, `j` 변수는 각각 `nums`에서 `target`이 있을 가능성이 있는 범위의 하한, 상한을 가리며, `i` 이상, `j` 이하로 정의
- while 반복문과 그 안 내용을 위와 같이 설정하면, 어떤 케이스라도 반드시 `i > j`가 되는 순간이 발생하며, 그 때의 `i`가 `target`이 있거나 또는 `target`이 오름차순 유지한 채 들어갈 수 있는 인덱스가 됨
- 참고로 while 반복문 안쪽 if 조건문에 `nums[m] == target`에 대한 별도 처리가 없음, 조건문을 보면 `j`를 조정하게 됨
- 만일 `nums`가 아래와 같고 `target`이 7인 경우...
```plaintext
nums = [2, 3, 5, 7, 7, 7, 7, 7, 11, 13]
target = 7
```
- 위 코드 반복문의 결과 `i`는 제일 왼쪽에 있는 7이 위치한 인덱스인 3이 되며, 만일 `nums[m] == target`일 때 `i`를 조정하도록 했다면, 반복문의 결과 `i`는 제일 오른쪽에 있는 7이 위치한 인덱스의 다음 인덱스인 8이 됨

### 재귀호출로 이진 탐색
- 반복문을 재귀호출 방식으로 변경, 알고리즘도 동일
- 시간복잡도는 반복문 방식과 동일하나 공간복잡도에 차이가 있음, 반복문 방식은 O(1), 재귀호출 방식은 O(log N)이 됨 (재귀 호출 스택 때문)
```python
# 런타임 0 ms, 메모리 19.8 MB
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        def f(i, j):
            if i > j:
                return i

            m = i + (j-i)//2
            if nums[m] < target:
                return f(m+1, j)
            else:
                return f(i, m-1)

        return f(0, len(nums)-1)
```