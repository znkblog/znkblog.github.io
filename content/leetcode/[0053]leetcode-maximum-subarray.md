---
title: "leetcode: 53. Maximum Subarray"
description: "nums 배열의 연속된 원소들로 부분배열을 만들었을 때, 부분배열의 합 중 최대값을 구하는 문제"
updated: "2026-10-21"
tags: ["leetcode", "array", "divide_and_conquer", "dynamic_programming"]
---

## 문제

[https://leetcode.com/problems/maximum-subarray](https://leetcode.com/problems/maximum-subarray)

`nums` 배열의 연속된 원소들로 부분배열을 만들었을 때, 부분배열의 합 중 최대값(최대 부분합)을 구하는 문제다.

동적 계획법과 분할 정복을 사용해서 풀 수 있다.

## 동적 계획법(Dynamic Programming)
```python
# 런타임 55 ms, 메모리 31.4 MB
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        a = [0] * len(nums)
        a[0] = nums[0]

        for i, x in enumerate(nums[1:], 1):
            a[i] = max(a[i-1] + x, x)

        return max(a)
```
[동적 계획법](/post/coding-test-basic#동적-계획법dynamic-programming)은 초기값과 일반항을 정의해서 풀 수 있다.

`nums`의 `i`번째 인덱스를 제일 마지막 원소로 하는 부분배열의 합 중 최대값을 `a[i]`라 했을 때 초기값과 일반항은 아래와 같다.
> - 초기값: a[0] = nums[0]
> - 일반항: a[i] = max(a[i-1] + nums[i], nums[i])

일반적으로 합산되는 원소가 많아질수록 합의 결과는 증가하나, 큰 음수가 섞여 있는 경우 때에 따라서는 음수 부분을 끊고 새롭게 다음 숫자부터 합산을 시작하는 것이 나을 수도 있는데, 위 일반항은 이를 반영한 수식이다.

위와 같이 최대 부분합을 구하는 동적 계획법을 특별히 [카데인 알고리즘(Kadane's Algorithm)](https://en.wikipedia.org/wiki/Maximum_subarray_problem)이라고도 한다.

위 코드에서는 `a[i]`들을 계산한 다음 이들 중 최대값(최대 부분합)을 리턴하도록 되어 있다.

## 분할 정복(Divide and Conquer)
```python
# 런타임 251 ms, 메모리 31.6 MB
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return f(nums)[1]

def f(nums: List[int]) -> (int, int, int, int):
    if len(nums) == 1:
        return nums[0], nums[0], nums[0], nums[0]

    m = len(nums) // 2
    Xl, Xm, Xr, Xt = f(nums[:m])
    Yl, Ym, Yr, Yt = f(nums[m:])

    return max(Xl, Xt+Yl), max(Xm, Xr+Yl, Ym), max(Xr+Yt, Yr), Xt+Yt
```

`f` 함수가 [분할 정복](/post/coding-test-basic#분할-정복divide-and-conquer)을 수행하는 재귀함수다.

나뉘어진 두개의 배열 X, Y를 다시 하나로 합치는 과정에서 X의 최대 부분합을 `Xm`, Y의 최대 부분합을 `Ym`이라 했을 때, X+Y의 최대 부분합은 `Xm`, `Ym` 둘중 하나가 아니라 하나의 케이스를 더 봐야 한다. 아래 예시로 설명해보자.

```plaintext
X                  Y
[4, 2, 3, -20, 7], [3, 2, -20, 5, 5]
```

위 예시에서 `Xm`은 9, `Ym`은 10이지만, X+Y의 최대 부분합은 12(= 7+3+2)가 된다. 즉 X의 가장 오른쪽 원소를 포함한 최대 부분합 `Xr` 7과 Y의 가장 왼쪽 원소를 포함한 최대 부분합 `Yl` 5의 합으로 수식으로 나타내면 `max(Xm, Xr + Yl, Ym)`이다.

X+Y는 이제 다음 재귀호출 과정에서 예를들면 Z+W와 같은 배열과 다시 최대 부분합을 구하게 된다. 위 수식과 유사하게 표현하면 `max((X+Y)m, (X+Y)r + (Z+W)l, (Z+W)m)`이 될 것이다.

`(X+Y)r`은 X+Y의 가장 오른쪽 원소를 포함한 최대 부분합이므로 `Yr`이라고 생각할 수 있으나 하나를 더 비교해야 한다. X 배열이 더해진 효과를 감안한 `Xr + Yt`인데 `Yt`는 Y 배열 전체 합계를 뜻한다. `Xr + Yt`가 `Yr` 보다 더 클 경우 `(X+Y)r`은 `Xr + Yt`가 될 수 있다. 즉 수식으로 표현하면 `(X+Y)r = max(Xr + Yt, Yr)`이다.

참고로 `(Z+W)l`도 유사하게 생각해보면, `max(Zl, Zt + Wl)`이 된다.

종합하면 분할정복 과정에서 다음 단계로 넘겨야 할 정보들은 어떤 A 배열 기준으로 A 의 가장 왼쪽 원소가 포함된 최대 부분합 `Al`, A 의 현시점 최대 부분합 `Am`, A 의 가장 오른쪽 원소가 포함된 최대 부분합 `Ar`, A 원소의 전체합계 `At`이다. (처음 볼 땐 어려웠지만 차근차근 잘 생각해보면 어느순간 이해가 될 것이다.)

위 python 코드도 이를 반영하여 4개 값을 튜플로 모아서 리턴한다.