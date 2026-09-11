---
title: "동적계획법 (Dynamic Programming) 과 메모이제이션 (Memoization)"
description: "수학 점화식과 유사한 귀납적 풀이 방식으로 문제를 해결하는 알고리즘인 동적계획법과 이미 한번 진행한 계산을 다시 할 필요가 없도록 하는 메모이제이션 기법"
updated: "2026-09-10"
---

## 동적계획법

고등학교 수학에서 점화식을 배운 적 있음, 간단하게 얘기하자면 어떤 함수 F 가 초기 단계의 반환값은 고정값으로 정의, N 번째 단계의 반환값은 그 이전 단계의 반환값과의 관계에 의해 결정된다고 할 때, 문제를 풀어내는 방식임,

초기 단계의 반환값을 `초기값`이라 했고, N 번째 단계의 반환값을 `일반항`이라 불렀던 게 기억이 남,

자연수 N 까지의 곱셈의 결과를 반환하는 팩토리얼 함수 F 를 이와 같은 식으로 표현하면 아래와 같이 됨,

> - 초기값: F(1) = 1
> - 일반항: F(N) = F(N-1) * N

굳이 점화식 얘기를 꺼내는 이유는, 본 포스팅에서 소개하고자 하는 동적계획법은 [나무위키](https://namu.wiki/w/%EB%8F%99%EC%A0%81%20%EA%B3%84%ED%9A%8D%EB%B2%95) 과 같은 설명을 아무리 들여다봐도 전혀 이해가 안됐었고, 그냥 고등학교 때 배웠던 **점화식이 곧 동적계획법**이라는 것이 더 이해가 빨랐기 때문임,

또한 동적계획법의 영문 이름은 Dynamic Programming 인데, 영어단어와 한글단어가 정확히 매칭되는 것도 아니고, 점화식 풀이에 가까운 알고리즘이 왜 동적계획법이라는 이름이 붙어있는 건지도 잘 모르겠음,

## 메모이제이션

동적계획법은 크게 초기값부터 시작해서 N 단계를 풀어가는 Bottom-Up 방식과, N 단계에서 시작해서 거꾸로 되짚어가는 Top-Down 방식이 있음, 각각 반복문을 사용하는 itertive 방식과 재귀함수를 사용하는 recursive 방식으로 연결 됨,

그런데, recursive 방식은 필연적으로 재귀함수를 사용하게 되는데, 재귀함수는 스택 호출 제한에 걸리기 딱 좋은 케이스가 많음, 특히 동일한 계산을 자주하게 되는 경우 상당히 비효율인데, 이를 방지하기 위한 방법이 **한번 계산한 결과는 기억해뒀다가 다시 재활용**하는 메모이제이션임,

즉 위에 언급한 팩토리얼 함수에서 F(5) 의 값은 120 이라고 한번 계산이 되었다면, 재귀호출로 다시 F(5) 가 호출될 때 굳이 재계산 할 필요없이, 사전에 저장해 놓은 120 을 그대로 사용하는 것임, (물론 팩토리얼 같은 간단한 동적계획법 정도는 굳이 메모이제이션을 쓸 필요는 없긴 함)

## leetcode: 70. Climbing Stairs

[https://leetcode.com/problems/climbing-stairs/](https://leetcode.com/problems/climbing-stairs/)

계단을 오르는 방법이 한번에 한계단씩 오르는 방법과 한번에 두계단씩 오르는 방법이 있다고 할 때, 전체 n 개 계단을 오르는 케이스 가짓수를 찾는 문제,

n 개 계단을 오르는 방법을 생각해보면, n-1 계단까지 오르고 나서 마지막 한계단을 오르는 방법이 있고, n-2 계단까지 오르고 나서 마지막 두계단을 한번에 오르는 방법이 있음, 즉 동적계획법으로 생각해보면 초기값과 일반항은 아래와 같음,

> - 초기값: F(1) = 1, F(2) = 2
> - 일반항: F(n) = F(n-2) + F(n-1)

iterative 방식으로 풀면 아래와 같음,

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a = {}
        a[1], a[2] = 1, 2

        for i in range(3, n+1):
            a[i] = a[i-2] + a[i-1]

        return a[n]
```

a 딕셔너리를 상정, 초기값을 미리 저장하고, 이후부터 반복문으로 단계를 계속 올려가며 n 단계까지 계산하는 방식임,

결과적으로 a 딕셔너리 안에 1 부터 n 까지의 계단 오르는 가짓수가 모두 저장되게 되는데, 최종 n 단계의 값만 필요하다면 아래처럼 더 간단히 풀어낼 수 있음,

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2

        for i in range(2, n+1):
            a, b = b, a+b
        
        return a
```

이해가 잘 안 될 수도 있지만, 위와 같은 로직 적용하면 a 변수에 i 단계의 계단 오르는 가짓수가 계속 업데이트됨,

이제 recursive 방식을 적용해 보면 아래와 같음, 그러나 이 풀이는 시간초과 에러로 풀리지 않음,

``` python
class Solution:
    def climbStairs(self, n: int) -> int:
        def f(i: int) -> int:
            return i if i < 3 else f(i-2) + f(i-1)

        return f(n)
```

f 함수가 동적계획법을 풀어내는 재귀함수임, 시간초과가 나는 이유는 간단한데, 예를들어 `f(20)` 을 호출한다고 하면 `f(19) + f(18)` 이 리턴 됨,

다시 `f(19)` 와 `f(18)` 을 호출하므로 각각 `f(18) + f(17)` 과 `f(17) + f(16)` 을 리턴함, 앞 return 구문에도 `f(17)` 이 있고 뒤 return 구문에도 `f(17)` 이 있음, 즉 한번 계산했던 걸 또 계산하게 됨, n 이 크다면 또 계산해야 하는 단계는 기하급수적으로 늘어날 수밖에 없음,

앞 return 구문에서 `f(17)` 을 계산한 결과를 저장소에 넣어뒀다가, 뒤 return 구문에서는 그냥 저장소에서 그 결과를 빼내오기만 하면 훨씬 효율적이 됨, 이 방식이 메모이제이션임,

아래는 메모이제이션을 python 의 데코레이터 문법으로 구현한 풀이임,

```python
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

        return f(n)
```

memoize 함수가 메모이제이션 핵심임, h 딕셔너리를 저장소로 활용, f(n) 의 결과가 h 안에 있는지 검사해서 없다면 계산해서 저장소에 넣어 둠, 언제나 h 딕셔너리에 저장된 결과를 리턴하게 됨,

memoize 함수가 실제 문제를 풀어내는 f 함수를 래핑하도록 되어 있음,

참고로 python 은 라이브러리를 통해 빌트인으로 메모이제이션 함수를 제공함, 아래는 이를 사용한 풀이임,

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def f(i: int) -> int:
            return i if i < 3 else f(i-2) + f(i-1)

        return f(n)
```

본래 functools 라이브러리를 임포트해야 하지만, leetcode 에서는 대부분의 라이브러리가 자동으로 임포트되어 있음,

## leetcode: 118. Pascal's Triangle

[https://leetcode.com/problems/pascals-triangle/](https://leetcode.com/problems/pascals-triangle/)

위 링크를 들어가보면, 움짤만으로도 뭘 리턴해야 하는지 쉽게 알 수 있음,

초기값과 일반항은 아래와 같음,

> - 초기값: a[1] = [1]
> - 일반항: a[n] = [0, ...a[-1]] + [...a[-1], 0] (동일한 인덱스 요소끼리 더하여 새로운 배열 생성)

일반항 부분이 이해가 어려울 수 있는데, 예를들면 n 이 4 라면, n 이 3 일때의 결과인 [1, 2, 1] 을 사용하여, [0, 1, 2, 1] 리스트와 [1, 2, 1, 0] 리스트를 만든 다음, 동일한 인덱스 요소끼리 더하는 방식임, 즉 [1, 3, 3, 1] 이 됨,

iterative 방식으로 아래와 같이 풀 수 있음,

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [[1]]

        for i in range(2, numRows+1):
            t1 = [0, *a[-1]]
            t2 = [*a[-1], 0]
            a.append([x+y for x, y in zip(t1, t2)])
 
        return a
```

a 리스트에 1 부터 numRows 단계까지의 결과를 누적해서 리턴하도록 되어 있음,