---
title: "leetcode: 994. Rotting Oranges"
description: "grid 안에 있는 썩은 오렌지가 매분마다 상하좌우에 있는 다른 오렌지를 썩게 만들 때 몇분만에 모든 오렌지를 썩게 만드는지 구하는 문제"
updated: "2026-10-xx"
tags: ["leetcode", "array", "breadth_first_search", "matrix"]
---

## 문제
- [https://leetcode.com/problems/rotting-oranges](https://leetcode.com/problems/rotting-oranges)
- `grid` 안에 있는 썩은 오렌지가 매분마다 상하좌우에 있는 다른 오렌지를 썩게 만들 때 몇분만에 모든 오렌지를 썩게 만드는지 구하는 문제
- `grid` 각 공간에는 썩은 오렌지 2, 일반 오렌지 1, 비어있는 공간 0으로 채워져있음
- 모든 오렌지가 썩을 때까지 최소 몇분 걸리는지 리턴, 만일 모든 오렌지를 썩게하지 못한다면 -1 리턴

## 너비우선탐색(Breadth First Search)
```python
# 런타임 0 ms, 메모리 19.4 MS
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        count = 0
        qu = [(y, x, 0) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == 2]

        while qu:
            (y, x, c) = qu.pop(0)
            for (dy, dx) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if 0 <= y + dy < len(grid) and 0 <= x + dx < len(grid[0]) and grid[y + dy][x + dx] == 1:
                    count = c + 1
                    grid [y + dy][x + dx] = 2
                    qu.append((y+dy, x+dx, count))

        if any(grid[y][x] == 1 for y in range(len(grid)) for x in range(len(grid[0]))):
            return -1

        return count
```
- 큐 자료구조와 반복문으로 [너비우선탐색](https://namu.wiki/w/%EB%84%88%EB%B9%84%20%EC%9A%B0%EC%84%A0%20%ED%83%90%EC%83%89) 구현, 큐를 나타내는 `qu`에는 썩은 오렌지가 담기게 되는데 `(y좌표, x좌료, 경과된시간)` 형식의 튜플로 썩은 오렌지 정보 표현
- while 반복문 직전에 `qu`에 `grid` 안 썩은 오렌지 초기 정보를 담음, 처음부터 썩어있었기 때문에 경과된 시간은 0임
- `qu`에서 꺼낸 썩은 오렌지 정보를 기반으로 상하좌우를 탐색함, 상하좌우 좌표가 `grid`에서 유효한 좌표이면서 일반 오렌지가 위치해있다면, 경과시간을 하나 늘리고 썩은 오렌지로 업데이트 한 뒤, 다시 `qu`에 삽입
- while 반복문 종료 후 `grid` 안에 일반 오렌지가 하나라도 남아있다면 모든 오렌지를 썩히지 못했으므로 -1 리턴, 아니라면 전체 경과시간인 `count`를 리턴