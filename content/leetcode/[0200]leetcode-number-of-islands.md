---
title: "leetcode: 200. Number of Islands"
description: "이차원 매트릭스로 주어지는 grid에서 '1'은 육지를 '0'은 바다를 의미한다고 할 때, 섬의 개수를 리턴하는 문제"
updated: "2026-11-02"
tags: ["leetcode", "breadth_first_search", "depth_first_search", "matrix", "union_find"]
---


## 문제
[https://leetcode.com/problems/number-of-islands](https://leetcode.com/problems/number-of-islands)

이차원 매트릭스로 주어지는 `grid`에서 `"1"`은 육지를 `"0"`은 바다를 의미한다고 할 때, 섬의 개수를 리턴하는 문제입니다.

`grid` 바깥은 모두 바다이고, 육지의 상하좌우가 육지일 땐 연결된 육지로 봅니다.


## 너비우선탐색(BFS, Breadth First Search)
```python
# 런타임 247 ms, 메모리 21.24 MB
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count = 0
        maxy, maxx = len(grid), len(grid[0])

        for y, x in ((y, x) for y in range(maxy) for x in range(maxx)):
            if grid[y][x] != "1":
                continue

            qu = [(y, x)]
            grid[y][x] = "2"
            count += 1

            while qu:
                y, x = qu.pop(0)

                for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    if (
                        0 <= y + dy < maxy
                        and 0 <= x + dx < maxx
                        and grid[y + dy][x + dx] == "1"
                    ):
                        grid[y + dy][x + dx] = "2"
                        qu.append((y + dy, x + dx))

        return count
```

[큐](https://namu.wiki/w/%ED%81%90(%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0)) 자료구조로 [BFS](https://namu.wiki/w/%EB%84%88%EB%B9%84%20%EC%9A%B0%EC%84%A0%20%ED%83%90%EC%83%89) 알고리즘을 구현하여 풀었습니다.

`grid` 전체를 순회하면서, 육지인 `"1"`을 만나면 해당 지역의 상하좌우도 육지인지를 검사하고 큐를 나타내는 `qu` 배열에 삽입합니다. 그리고 한 번 방문한 지역은 `"2"`로 표시하여 중복 방문이 되지 않도록 합니다.

BFS 과정에서 육지와 연결된 육지(즉 동일한 섬인 지역)는 모두 `"2"`로 방문처리가 되므로, 새로운 육지 `"1"`을 만나면 또 다른 섬이라는 의미가 됩니다.

전체적인 코드 로직은 `"1"`을 만날 때마다 `count`를 늘리고 BFS로 동일한 섬 지역을 모두 처리하는 식으로 모든 지역을 방문한 뒤 마지막에 `count`를 리턴하는 구조로 되어 있습니다.


## 깊이우선탐색(DFS, Depth First Search)
```python
# 런타임 219 ms, 메모리 21.67 MB
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count = 0
        maxy, maxx = len(grid), len(grid[0])

        def f(tup):
            y, x = tup
            for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if (
                    0 <= y + dy < maxy
                    and 0 <= x + dx < maxx
                    and grid[y + dy][x + dx] == "1"
                ):
                    grid[y + dy][x + dx] = "2"
                    f((y + dy, x + dx))

        for y, x in ((y, x) for y in range(maxy) for x in range(maxx)):
            if grid[y][x] != "1":
                continue

            grid[y][x] = "2"
            count += 1

            f((y, x))

        return count
```

[스택](https://namu.wiki/w/%EC%8A%A4%ED%83%9D(%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0)) 자료구조를 사용하는 [DFS](https://namu.wiki/w/%EA%B9%8A%EC%9D%B4%20%EC%9A%B0%EC%84%A0%20%ED%83%90%EC%83%89) 방식 풀이로 재귀함수를 사용했습니다.

참고로 위 챕터의 BFS 코드에서 `qu.pop(0)`을 `qu.pop()`으로 고치기만 해도 동일한 DFS 방식 코드가 되지만, DFS는 함수 스택을 사용할 수도 있어 BFS로는 불가능한 재귀함수로 문제를 풀었습니다.

어떤 육지에 상하좌우로 인접한 육지를 탐색하는 순서만 다를 뿐 BFS 코드와 유사한 로직으로 문제를 해결합니다.


## 유니온 파인드(Union Find)
```python
# 런타임 251 ms, 메모리 25.43 MB
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count = sum(row.count("1") for row in grid)
        maxy, maxx = len(grid), len(grid[0])
        parent = list(range(maxy * maxx))
        rank = [1] * (maxy * maxx)

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(a, b):
            # 리턴값: 0이면 이미 동일한 그룹, 1이면 새롭게 같은 그룹으로 편입
            ra, rb = find(a), find(b)

            if ra == rb:
                return 0

            if rank[ra] < rank[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            rank[ra] = max(rank[ra], rank[rb] + 1)
            return 1

        for y, x in ((y, x) for y in range(maxy) for x in range(maxx)):
            if grid[y][x] == "1":
                idx = maxx * y + x
                if x + 1 < maxx and grid[y][x + 1] == "1":
                    count -= union(idx, idx + 1)
                if y + 1 < maxy and grid[y + 1][x] == "1":
                    count -= union(idx, idx + maxx)

        return count
```

[유니온 파인드](https://namu.wiki/w/Union-Find) 자료구조를 사용해서 문제를 풀 수도 있습니다. 유니온 파인드에서 필수인 find와 union 함수를 각각 구축한 뒤 인접한 육지끼리는 union을 하는 방식입니다.

`grid`에서 육지 `"1"`의 전체 개수를 `count`에 담은 뒤, 인접 육지로 판단될 때마다 `count`를 차감하는 방식으로 섬의 개수를 구합니다.

또한 `grid` 좌상단부터 전체를 한 번은 순회하게 되므로 효율을 위해 인접 육지를 판단할 때 오른쪽과 아래쪽만 판단하도록 했습니다.