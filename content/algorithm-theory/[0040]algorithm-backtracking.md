---
title: "백트래킹"
description: "가능한 선택을 탐색하고 정답이 될 수 없는 경로를 가지치기하는 알고리즘"
updated: "2026-10-27"
tags: ["알고리즘", "백트래킹", "깊이우선탐색", "algorithm", "backtracking", "depth_first_search"]
---

## 백트래킹(Backtracking)
- 백트래킹은 정답에 해당하는 케이스(경우의 수)를 찾기 위해, 순서대로 케이스를 만들어가는 선택을 하나씩 시도하다가 **정답에 도달할 수 없다고 판단되면 현재의 선택을 포기(가지치기)하고 이전 단계로 돌아가 다른 선택을 시도하는 알고리즘** 기법
- 아래와 같은 방식으로 동작
> - 하나의 케이스 조립을 위해 현 단계에서 가능한 선택지 확인
> - 선택지 중 하나를 선택하고 다음 과정 진행
> - 만일 해당 선택지로는 답에 도달할 수 있는 케이스 조립이 불가능하다고 판단되면 해당 선택지를 버리고 이전 과정으로 복귀
> - 케이스 조립이 완성이 되었다면 해당 케이스를 처리
- 즉 케이스를 만드는 과정에서, 답이 될 수 있는지를 지속적으로 판단하여, 불필요한 케이스까지 만들어내는 비효율을 없애는 방식으로, 모든 케이스를 무조건 끝까지 만들어보고나서 답인지 아닌지를 확인하는 완전 탐색과 차이가 있음
- 선택지를 탐색하고 이전 선택으로 돌아가고 하는 과정 포함되어있어 DFS(깊이우선탐색) 및 재귀함수와 관련성이 높음

## leetcode: 46. Permutations
### 문제
- [https://leetcode.com/problems/permutations](https://leetcode.com/problems/permutations)
- 중복없는 숫자로 채워진 `nums` 배열에서 각 원소를 모두 사용하여 만들어 낼 수 있는 순열 전체를 리턴하는 문제

### 완전 탐색
- 모든 케이스를 만들어 놓고, 답에 해당하는 케이스만 고른 뒤 리턴
```python
# 런타임 46 ms, 메모리 25.6 MB
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        a = [[]]
        for _ in range(0, len(nums)):
            t = []
            for x in a:
                for y in nums:
                    t.append(x[:] + [y])
            a = t

        a = [x for x in a if len(set(x)) == len(x)]
        return a
```
- 예를들어 `nums`가 `[1, 2, 3]`이라고 한다면 아래와 같은 알고리즘 적용
> - `a`를 `[[]]` 배열로 시작, `nums`의 각 원소를 삽입하여 `[[1], [2], [3]]`을 생성
> - `a`의 각 원소인 `[1]`, `[2]`, `[3]`에 다시 `nums`의 각 원소를 삽입하여 `[[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3]]` 생성
> - `a`의 각 원소에 다시 `nums`의 각 원소를 삽입하여 `[[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 1], [1, 2, 2], [1, 2, 3], ... ]` 생성
> - 마지막에 `a` 안 원소에서 순열의 조건을 충족하지 못하는 케이스들을 삭제
- 순열의 특성상 동일한 원소가 중복 사용되어서는 안되므로, 중복된 값이 있는지는 검사하는 방식으로 순열에 부합하지 않는 케이스들을 걸러냄

### BFS(너비우선탐색) + 가지치기(Pruning) 적용
- 케이스를 만들어 가는 과정에서 조건 검사하여 가지치기 적용
```python
# 런타임 1 ms, 메모리 19.5 MB
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        a = [[]]
        for _ in range(0, len(nums)):
            t = []
            for x in a:
                for y in nums:
                    if y in x:
                        continue

                    t.append(x[:] + [y])
            a = t

        return a
```
- 완전 탐색과 동일한 과정이나, 가장 안쪽 루프에서 중복값이 케이스로 조립이 될 지 검사하는 로직을 if 조건문으로 검사
- 중복값이 사용된다면 continue 구문을 통해 케이스로 조립이 되는 것을 포기(즉 가지치기)하고 다음 케이스 진행
- 케이스 생성하는 과정에서 순열 조건식을 판단했기 때문에, 최종 형성된 `a` 배열을 그대로 리턴

### 재귀호출 사용 백트래킹
- DFS(깊이우선탐색) 방식의 재귀호출을 사용하여 가지치기 + 이전 선택으로 돌아가는 완전한 백트래킹 적용
```python
# 런타임 1 ms, 메모리 19.4 MB
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        a = []
        def backtracking(case):
            if len(set(case)) != len(case):
                return

            if len(case) == len(nums):
                a.append(case)
                return
            
            for x in nums:
                backtracking(case[:] + [x])

        backtracking([])
        return a
```
- `backtracking` 재귀함수가 백트래킹을 수행하는 핵심 재귀함수, 첫번째 if 조건문에서 가지치기하고 기존 호출 스택으로 복귀(즉 이전 선택으로 복귀)함
- 두번째 if 조건문에선 케이스가 완성되었는지 판단하고, 그 아래 for 반복문에서는 재귀호출을 수행
- 위 코드에서 첫번째 if 조건문을 삭제하고 for 반복문 안에서 중복 여부를 검사(for 구문 안에서만 가지치기)할 수도 있음, 이 경우 BFS + 가지치기 코드와 상당히 유사하나 그래도 탐색 방법은 재귀호출을 이용한 DFS임