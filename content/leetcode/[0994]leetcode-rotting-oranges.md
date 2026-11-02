---
title: "leetcode: 994. Rotting Oranges"
description: "이차원 매트릭스로 주어지는 grid에 오렌지들이 있고, 그 중 썩은 오렌지가 신선한 오렌지를 썩게 만들 때, 전체 오렌지가 썩게 되는 시간을 리턴하는 문제"
updated: "2026-11-03"
tags: ["leetcode", "array", "breadth_first_search", "matrix"]
---


## 문제
[https://leetcode.com/problems/rotting-oranges](https://leetcode.com/problems/rotting-oranges)

이차원 매트릭스로 주어지는 `grid`에 오렌지들이 있고, 그 중 썩은 오렌지가 신선한 오렌지를 썩게 만들 때, 전체 오렌지가 썩게 되는 시간을 리턴하는 문제입니다.

썩은 오렌지는 2, 신선한 오렌지는 1로 표기되어 있으며, 매 분마다 썩은 오렌지의 상하좌우에 있는 신선한 오렌지도 썩게 된다고 합니다.

`grid` 안 전체 오렌지가 썩게 되는 최소 시간(분)을 리턴하되, 만일 전체 오렌지가 썩을 수 없다면 -1을 리턴하도록 합니다.


## 너비우선탐색(BFS, Breadth First Search)
```python
# 런타임 3 ms, 메모리 19.24 MB
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        maxy, maxx = len(grid), len(grid[0])
        fresh, minute = 0, 0
        qu = []
        for y in range(maxy):
            for x in range(maxx):
                match grid[y][x]:
                    case 1:
                        fresh += 1
                    case 2:
                        qu.append((y, x, 0))

        while qu:
            y, x, m = qu.pop(0)

            for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if (
                    0 <= y + dy < maxy
                    and 0 <= x + dx < maxx
                    and grid[y + dy][x + dx] == 1
                ):
                    grid[y + dy][x + dx] = 2
                    qu.append((y + dy, x + dx, m + 1))
                    minute = max(minute, m + 1)
                    fresh -= 1

        return -1 if fresh > 0 else minute
```

[큐](https://namu.wiki/w/%ED%81%90(%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0)) 자료구조를 사용하는 [BFS](https://namu.wiki/w/%EB%84%88%EB%B9%84%20%EC%9A%B0%EC%84%A0%20%ED%83%90%EC%83%89) 알고리즘을 사용했습니다. 일반적으로 최단거리 또는 최단시간 탐색에 BFS가 사용됩니다.

우선 `grid` 탐색하여, 신선한 오렌지 개수를 `fresh`에 저장하고, 썩은 오렌지를 `(y좌표, x좌표, 썩게 된 시간(분))` 튜플 형태로 큐 자료구조로 사용되는 `qu` 배열에 저장합니다.

while 반복문으로 BFS 탐색을 진행하면서 썩은 오렌지의 상하좌우에 신선한 오렌지가 있다면, 해당 오렌지를 썩히고 큐에 새로 썩게 된 오렌지 정보를 삽입하고 경과된 시간(분)을 업데이트하고 신선한 오렌지 수를 줄입니다.

마지막에 신선한 오렌지가 남아있는지 체크하여 -1 또는 오렌지가 썩기까지 경과된 시간(분)을 리턴합니다.
