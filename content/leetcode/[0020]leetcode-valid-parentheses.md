---
title: "leetcode: 20. Valid Parentheses"
description: "소·중·대 괄호만으로 이뤄진 문자열 s가 올바른 괄호쌍으로 이뤄져 있는지를 판별하는 문제"
updated: "2026-10-31"
tags: ["leetcode", "stack", "string"]
---


## 문제
[https://leetcode.com/problems/valid-parentheses](https://leetcode.com/problems/valid-parentheses)

소·중·대 괄호만으로 이뤄진 문자열 `s`가 올바른 괄호쌍으로 이뤄져 있는지를 판별하는 문제다.

문제에서 말하는 "올바른 괄호쌍"은 아래와 같다.
> - 여는 괄호는 반드시 같은 종류의 닫는 괄호로 닫혀야 함
> - 여는 괄호는 반드시 올바른 순서로 닫혀야 함
> - 모든 닫는 괄호는 같은 종류의 대응하는 여는 괄호가 있어야 함


## 올바른 괄호쌍 계속 삭제
```python
# 런타임 62 ms, 메모리 19.18 MB
class Solution:
    def isValid(self, s: str) -> bool:
        p = ""

        while p != s:
            p = s
            s = s.replace("()", "").replace("{}", "").replace("[]", "")

        return p == ""
```

문자열 `s`에서 올바른 괄호쌍을 계속 지워간다. 미리 `p`에 `s` 내용을 할당한 뒤, 더 이상 변동이 없을 때(즉 `p == s`일 때) while 반복문을 탈출한다.

올바른 괄호쌍만 있었다면 모두 지워졌을 것이므로 `p`가 비어 있는지를 검사한다.


## 스택(Stack)
```python
# 런타임 0 ms, 메모리 19.08 MB
class Solution:
    def isValid(self, s: str) -> bool:
        ht = {")": "(", "}": "{", "]": "["}
        st = []

        for x in s:
            if x in ht:
                if not st or st.pop() != ht[x]:
                    return False
            else:
                st.append(x)

        return len(st) == 0
```

`st` 배열은 [스택](https://namu.wiki/w/%EC%8A%A4%ED%83%9D(%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0)) 자료구조로 여는 괄호만을 저장한다. 괄호 종류는 `{ 닫는 괄호: 여는 괄호, ... }` 형태로 미리 `ht` 딕셔너리에 저장해 두었다.

for 반복문으로 순회할 때, 여는 괄호라면 `st`에 삽입하고 닫는 괄호라면 `st`에서 여는 괄호를 꺼내 동일한 종류인지 비교한다.

스택의 후입선출(LIFO) 특성을 생각하면 가장 안쪽의 여는 괄호와 비교하게 되며, 모든 괄호가 올바른 괄호쌍이었다면 `st`는 비어 있어야 한다.