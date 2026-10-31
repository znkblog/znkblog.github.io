---
title: "leetcode: 70. Climbing Stairs"
description: "한번에 1 또는 2 계단만 오를 수 있다고 할 때, n개 계단을 오르는 방법 가짓수를 구하는 문제"
updated: "2026-10-21"
tags: ["leetcode", "dynamic_programming", "math", "memoization"]
---

## 문제
[https://leetcode.com/problems/climbing-stairs](https://leetcode.com/problems/climbing-stairs)

한번에 1 또는 2 계단만 오를 수 있다고 할 때, n개 계단을 오르는 방법 가짓수를 구하는 문제다.

## 반복문 사용 동적 계획법(Dynamic Programming)
```python
# 런타임 0 ms, 메모리 19.3 MB
class Solution:
    def climbStairs(self, n: int) -> int:
        a = {}
        a[1], a[2] = 1, 2

        for i in range(3, n+1):
            a[i] = a[i-2] + a[i-1]

        return a[n]
```
수학 점화식처럼 풀어내는 방법인 [동적 계획법](/post/coding-test-basic#동적-계획법dynamic-programming) 알고리즘을 반복문으로 구현했다.

`n`개 계단의 가짓수를 구하는 함수를 `f`라고 하면 아래와 같이 초기값, 일반항으로 표현할 수 있다. (피보나치 수열과 닮았다.)
> - 초기값: f(1) = 1, f(2) = 2
> - 일반항: f(n) = f(n-2) + f(n-1)

계단이 1개라면 오르는 방법 가짓수는 1개이며, 2개라면 1계단씩 오르는 방법과 2계단을 한번에 오르는 방법 2개가 있다.

계단이 `n`개라면 `n-2`계단까지 오른 뒤 남은 2계단을 한번에 오르는 방법과 `n-1`계단까지 오른 뒤 남은 1계단을 오르는 방법이 있어, 두 방법의 합계가 `n`계단 오르는 방법 가짓수가 된다.

위 코드에선 `a` 딕셔너리가 반복문 사용하여 `{ 계단수: 오르는방법가짓수, ... }` 형식으로 일반항 계산값을 저장해간다. 마지막엔 계산된 `n`계단 가짓수를 리턴한다.

## 반복문 사용 2
```python
# 런타임 0 ms, 메모리 19.2 MB
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2

        for i in range(2, n+1):
            a, b = b, a+b

        return a
```

중간 결과값 보관할 필요없이 `n`계단의 결과만 필요하다고 했을 때 적용할 수 있는 간편 버전이다. 계산 결과를 `a` 변수에 계속 업데이트하고 리턴한다.

## 메모이제이션(Memoization) 사용 재귀호출 방식
```python
# 런타임 0 ms, 메모리 19.1 MB
class Solution:
    def climbStairs(self, n: int) -> int:
        def memoize(f: Callable[int, int]) -> Callable[int, int]:
            h = {}
            def wrapper(n: int) -> int:
                if n not in h:
                    h[n] = f(n)
                
                return h[n]

            return wrapper

        @memoize
        def f(i: int) -> int:
            return i if i < 3 else f(i-2) + f(i-1)

        return f
```
`f` 함수는 재귀호출 방식으로 구현한 동적 계획법이 적용된 재귀함수다. `f` 함수만으로 `n`계단 오르는 가짓수를 구할 수는 있으나 시간 초과 에러 발생한다.

위 코드에서 `f(i-1)`을 계산하면 `f(i-3) + f(i-2)`가 되는데 이미 앞서 구한 `f(n-2)`를 또 구해야하는 지나친 중복 계산이 발생하기 때문이다. 따라서 한번 계산한 결과를 기억하고 있다가 재계산할 필요없이 재사용하는 [메모이제이션](/post/coding-test-basic#메모이제이션memoization) 기법을 활용하면 해결할 수 있다.

`memoize` 함수가 메모이제이션 기법을 적용한 래퍼 함수를 품고 있다. `n`의 계산 결과가 `h` 딕셔너리에 있는지 확인하여 없다면 먼저 계산을 하고, `h` 안에 있는 계산 결과를 리턴하도록 되어 있다. 이를 python 데코레이션 문법으로 `f` 함수를 감싸서 해결하였다.

## python 라이브러리로 메모이제이션
```python
# 런타임 0 ms, 메모리 19.3 MB
import functools

class Solution:
    def climbStairs(self, n: int) -> int:
        @functools.cache
        def f(i: int) -> int:
            return i if i < 3 else f(i-2) + f(i-1)

        return f(n)
```

python 제공 functools 라이브러리에 있는 cache 데코레이터를 메모이제이션으로 활용하였다. 더 상세한 내용은 [python 도움말](https://docs.python.org/ko/3/library/functools.html#functools.cache) 참고하자.

## 피보나치 수열 계산식 응용
```python
# 런타임 0 ms, 메모리 19.1 MB
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 5 ** 0.5
        b = (1+a) / 2
        c = round(b ** (n+1) / a)

        return c
```

본 문제의 초기값과 일반항을 보면 피보나치 수열과 매우 닮아있어, 피보나치 수열의 n번째 값을 직접 계산하는 공식인 [비네의 공식(Binet's Formula)](https://namu.wiki/w/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98%20%EC%88%98%EC%97%B4?from=%EB%B9%84%EB%84%A4%EC%9D%98%20%EA%B3%B5%EC%8B%9D)을 응용할 수 있다.

`c` 변수에서 `n+1` 대신 `n`을 사용하는 것이 본래의 피보나치 수열을 계산하는 것이지만 `n+1`을 넣으면 본 문제에서 요구하는 풀이가 된다. 또한 엄밀하게 얘기하면 `round` 함수는 비네의 공식에서는 나오지 않는 식이지만, 더 간편한 방법이 있음을 ai가 제시하여 사용했다.