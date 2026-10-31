---
title: "leetcode: 20. Valid Parentheses"
description: "소·중·대 괄호만으로 이뤄진 문자열 s가 올바른 괄호쌍으로 이뤄진 문자열인지 검사하는 문제"
updated: "2026-10-29"
tags: ["leetcode", "stack", "string"]
---

## 문제

[https://leetcode.com/problems/valid-parentheses](https://leetcode.com/problems/valid-parentheses)

소·중·대 괄호만으로 이뤄진 문자열 s가 올바른 괄호쌍으로 이뤄진 문자열인지 검사하는 문제다.

올바른 괄호쌍은 열린 괄호와 닫힌 괄호가 올바른 형태로 묶여있는 것으로, 예를들면 `(]`, `)(`, `([)]` 이런 문자열은 올바른 괄호쌍이 아니다.

## 올바른 괄호쌍 계속 제거
```python
# 런타임 59 ms, 메모리 19.2 MB
class Solution:
    def isValid(self, s: str) -> bool:
        p = ""

        while s != p:
            p = s
            s = s \
                .replace("()", "") \
                .replace("{}", "") \
                .replace("[]", "")

        return p == ""
```

문자열 `s`에서 올바른 괄호쌍인 `()`, `{}`, `[]`를 replace 함수로 계속 제거해 간다.

만일 더 이상 제거할 괄호가 없다면 `p == s`가 되므로 while 반복문을 종료한다.

`s`가 처음부터 올바른 괄호쌍만 있었다면, while 반복문을 거치면서 모두 제거가 될 것이므로, `p == ""`인지 판단하면 된다.

## 스택(Stack)
```python
# 런타임 1 ms, 메모리 19.3 MB
class Solution:
    def isValid(self, s: str) -> bool:
        h = {
            ")": "(", "}": "{", "]": "["
        }
        st = []

        for c in s:
            if c in h:
                if not(st and st.pop() == h[c]):
                    return False
            else:
                st.append(c)

        return len(st) == 0
```

[스택](/post/coding-test-basic#스택stack과-큐queue) 자료구조 용도로 `st` 배열 상정하였다. 문자열 `s`를 순회하면서, 열린괄호가 나온다면 일단 `st`에 삽입하고, 닫힌괄호가 나올 때 `st`을 pop하여 닫힌괄호와 매칭되는 열린괄호인지 체크하는 구조다.

닫힌괄호가 나왔을 때, `st`가 비어있거나, 매칭되는 열린괄호가 아니라면 더 이상 for 반복문을 수행할 필요없이 즉시 False 리턴한다.

올바른 괄호쌍만 있었다면 for 반복문을 마쳤을 때 `st`가 비어있게 된다. 그 여부를 판단하여 리턴한다.