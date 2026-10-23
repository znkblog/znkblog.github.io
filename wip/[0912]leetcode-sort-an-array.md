---
title: "leetcode: 912. Sort an Array"
description: "nums 배열의 숫자들을 오름차순으로 정렬하여 리턴하는 문제"
updated: "2026-10-xx"
tags: ["leetcode", "array", "divide_and_conquer", "heap", "sorting"]
---

## 문제
- [https://leetcode.com/problems/sort-an-array](https://leetcode.com/problems/sort-an-array)
- nums 배열의 숫자들을 오름차순으로 정렬하여 리턴하는 문제
- 추가로 언어가 자체 제공하는 정렬함수를 사용하지 말고, 시간복잡도 O(N log N)으로 풀 것도 요구하고 있음
- 아래 풀이보다 더 자세한 설명은 [정렬 알고리즘](https://namu.wiki/w/%EC%A0%95%EB%A0%AC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98) 참고 바람

## 버블 정렬(Bubble Sort)
```python
# 제한사항으로 실패
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(0, len(nums)-1):

            swapped = False
            for j in range(0, len(nums)-1-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True

            if not swapped:
                break

        return nums
```
- 아래와 같은 방식으로 정렬 수행
> - 0 인덱스 원소와 1 인덱스 원소를 비교, 0 인덱스 원소값 > 1 인덱스 원소값이라면 스왑
> - 1 인덱스 원소와 2 인덱스 원소를 비교, 1 인덱스 원소값 > 2 인덱스 원소값이라면 스왑
> - ...
> - N-2 인덱스 원소와 N-1 인덱스 원소를 비교, N-2 인덱스 원소값 > N-1 인덱스 원소값이라면 스왑
> - 이 결과 `nums` 안에서 가장 큰 값이 제일 N-1 인덱스(제일 마지막 자리)에 위치함
> - 다시 처음부터 N-2 인덱스 까지 동일한 비교를 반복, 이 결과 두번째로 큰 값이 N-2 번째에 위치함
> - 다시 처음부터 N-3 인덱스 까지 동일한 비교를 반복, 이 결과 세번째로 큰 값이 N-3 번째에 위치함
> - ...
- 이중 루프로 구현되어 있어 시간복잡도 O(N²)으로 풀리지는 않음, 동일한 값끼리 위치가 바뀌지 않기 때문에 안정 정렬
- `swapped` 변수로 중간에 스왑이 일어났는지를 파악함, 내부루프 반복 과정에서 스왑이 한번도 안일어났다면 이미 정렬이 되어 있는 상태라고 볼 수 있으므로 그 즉시 종료

## 선택 정렬(Selection Sort)
```python
# 제한사항으로 실패
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(0, len(nums)-1):

            minidx = i
            for j in range(i+1, len(nums)):
                if nums[minidx] > nums[j]:
                    minidx = j
            nums[i], nums[minidx] = nums[minidx], nums[i]

        return nums
```
- 아래와 같은 방식으로 정렬 수행
> - 0 ~ N-1 인덱스 중 가장 작은 원소값을 찾음, 0 인덱스 원소값과 가장 작은 원소값 스왑
> - 1 ~ N-1 인덱스 중 가장 작은 원소값을 찾음, 1 인덱스 원소값과 가장 작은 원소값 스왑
> - 2 ~ N-1 인덱스 중 가장 작은 원소값을 찾음, 2 인덱스 원소값과 가장 작은 원소값 스왑
> - ...
> - N-2 ~ N-1 인덱스 중 가장 작은 원소값을 찾음, N-2 인덱스 원소값과 가장 작은 원소값 스왑
> - 매 반복마다 앞에서부터 가장 작은 원소값들이 채워지게 됨
- 이중 루프로 구현되어 있어 시간복잡도 O(N²)으로 풀리지는 않음, 동일한 값끼리 위치가 바뀔 수 있기 때문에 불안정 정렬
- 불안정 정렬이 되는 예시는 아래와 같음
> - `[(20, "김"), (20, "이"), (10, "박")]`에서 튜플의 첫번째 원소로 오름차순 정렬
> - 내부루프 첫번째 반복 결과 `[(10, "박"), (20, "이"), (20, "김")]`이 됨
> - 내부루프 두번째 반복 결과 변동 없음
> - 최종적으로 앞쪽에 있던 `(20, "김")`이 `(20, "이")`보다 뒤쪽에 위치하게 됨
- 인접한 원소가 아닌 먼 거리의 스왑은 불안정 정렬이 되기 쉬움

## 삽입 정렬(Insertion Sort)
```python
# 제한사항으로 실패
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):

            key = nums[i]
            j = i - 1
            while 0 <= j and nums[j] > key:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key

        return nums
```
- 아래와 같은 방식으로 정렬 수행
> - 1 인덱스 원소와 보다 앞에있는 인덱스들 원소를 비교해서 삽입될 수 있는 위치에 삽입하고 삽입 이후 원소들을 하나씩 뒤로 보냄, 그 결과 0 ~ 1 인덱스가 정렬
> - 2 인덱스 원소와 보다 앞에있는 인덱스들 원소를 비교해서 삽입될 수 있는 위치에 삽입하고 삽입 이후 원소들을 하나씩 뒤로 보냄, 그 결과 0 ~ 2 인덱스가 정렬
> - ...
> - N-1 인덱스 원소와 보다 앞에있는 인덱스들 원소를 비교해서 삽입될 수 있는 위치에 삽입하고 삽입 이후 원소들을 하나씩 뒤로 보냄, 그 결과 0 ~ N-1 인덱스가 정렬

- "삽입"이라는 과정을 더 상세히 나타내면 아래와 같음
> - i 인덱스 원소 차례를 가정
> - i 인덱스 원소를 key 에 저장, 이 결과 i 인덱스 원소 자리는 비어있게 됨
> - key 와 i-1 인덱스 원소를 비교, `nums[i-1] <= key`일 경우 비어있는 i 인덱스에 key를 넣고 반복 종료, 아닐경우 i 인덱스에 i-1 인덱스의 원소값을 넣고 (이 결과 i-1 인덱스 원소 자리는 비어있게 됨) 반복 계속
> - key 와 i-2 인덱스 원소를 비교, `nums[i-2] <= key`일 경우 비어있는 i-1 인덱스에 key를 넣고 반복 종료, 아닐경우 i-1 인덱스에 i-2 인덱스의 원소값을 넣고 (이 결과 i-2 인덱스 원소 자리는 비어있게 됨) 반복 계속
> - ...
> - key 와 0 인덱스 원소를 비교, `nums[0] <= key`일 경우 비어있는 1 인덱스에 key를 넣고 반복 종료, 아닐경우 1 인덱스에 0 인덱스의 원소값을 넣고 (이 결과 0 인덱스 원소 자리는 비어있게 됨) 반복 계속
> - 더 이상 반복할 인덱스가 없으므로 0 인덱스 자리에 key 넣고 반복 종료
- 위 과정을 곰곰이 생각하면 바로 앞에 있는 인덱스 원소값과 비교해서 삽입될 위치가 아니라면 밀어내고 그 다음 앞에 있는 인덱스 원소값과 비교하고... 형태가 됨
- 이중 루프로 구현되어 있어 시간복잡도 O(N²)으로 풀리지는 않음, 동일한 값끼리 위치가 바뀌지 않기 때문에 안정 정렬

## 힙(Heap) 정렬
```python
# 런타임 891 ms, 메모리 27.6 MB
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        a = []
        for x in nums:
            a.append(x)

            c = len(a)-1
            p = (c - 1) // 2
            while 0 <= p and a[p] > a[c]:
                a[p], a[c] = a[c], a[p]
                c = p
                p = (c - 1) // 2

        for i in range(0, len(nums)):
            nums[i] = a[0]
            a[0] = a[-1]
            a.pop()

            p = 0
            c1 = 2*p + 1
            c2 = c1 + 1
            while c1 < len(a):
                c = c1 if len(a) <= c2 or a[c1] < a[c2] else c2
                if a[p] <= a[c]:
                    break

                a[p], a[c] = a[c], a[p]
                p = c
                c1 = 2*p + 1
                c2 = c1 + 1

        return nums
```
- 최소값이 루트에 위치하는 [최소힙](https://namu.wiki/w/%ED%9E%99%20%ED%8A%B8%EB%A6%AC) 자료구조를 사용, 루트가 항상 최소값을 보장하기 때문에 순서대로 추출해서 리턴하는 방식
- 코드 위쪽 `x`로 순회하는 for 반복문은 힙 자료구조에 데이터를 삽입하는 힙 푸시(heap push)를, 아래쪽 `i`로 순회하는 for 반복문은 힙 자료구조에서 데이터를 하나씩 뽑아내는 힙 팝(heap pop)을 구현함
- 참고로 0 인덱스를 힙 자료구조의 루트로 삼았음, 이 경우 부모 인덱스 `p`와 자식 인덱스 `c1`, `c2`의 관계는 아래와 같음 (위 링크 안 그림 설명은 1 인덱스를 루트로 삼고 있어 아래 수식과 다르니 주의)
``` plaintext
p = ((c1 or c2) - 1) // 2
c1 = (p + 1)*2 - 1 = 2*p + 1
c2 = c1 + 1
```
- 시간복잡도 O(N log N), 불안정 정렬
- 불안정 정렬이 되는 예시는 아래와 같음
> - `[(1, "A"), (1, "B"), (1, "C")]`에서 튜플 첫번째 원소를 오름차순으로 정렬한다고 했을 때, 이를 먼저 힙 자료구조로 만들면 동일하게 됨
> - 첫번째 원소를 힙 팝하고 난 후 힙 자료구조는 `[(1, "C"), (1, "B")]`가 되어, 두번째 원소가 기존의 순서를 앞질러서 먼저 나오게 됨

## in-place 방식 힙 정렬
```python
# 런타임 833 ms, 메모리 26.1 MB
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def sift_down(p, size):
            while (c := p*2 + 1) < size:
                if c+1 < size and nums[c] < nums[c+1]:
                    c = c+1
                if nums[p] >= nums[c]:
                    break

                nums[p], nums[c] = nums[c], nums[p]
                p = c

        n = len(nums)
        for p in range((n-2) // 2, -1, -1):
            sift_down(p, n)

        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            sift_down(0, i)

        return nums
```
- 앞선 힙 정렬은 별도의 배열을 생성하여 리턴하는 구조였으나, 위 코드는 `nums` 배열 자체를 in-place로 조작하는 방식
- 별도 메모리 생성을 하지 않기 위해, `nums` 자체를 최대힙 자료구조로 변경(루트에 가장 큰 값 위치), 힙 팝된 값들을 `nums` 뒤쪽부터 배치하는 방식으로 구현
- `sift-down` 함수는 `p`와 `size`를 넘겨주면, `p` 부모노드를 `size-1` 인덱스까지 최대힙에 걸맞도록 만들어주는 함수임, 단 `p` 노드만을 대상으로 하기 때문에 `p` 부터 `size-1`까지 모든 원소가 힙 자료구조가 되려면 모든 부모가 될 수 있는 노드에 대해 `sift-down` 함수를 걸어줘야 함
- `p`로 순회하는 for 반복문이 `nums` 모든 부모가 될 수 있는 원소들을 제일 아래쪽부터 모두 `sift-down` 해주는 구문임, 이 결과 `nums`는 최대힙 자료구조가 됨
- 그 아래 `i`로 순회하는 for 반목문은 루트(최대값이 있는 원소)를 힙 팝으로 빼내어 순서대로 뒤쪽부터 채우는 과정을 수행, `nums`를 오름차순 정렬이 되도록 함

## 퀵 정렬(Quick Sort)
```python
# 런타임 471 ms, 메모리 27.7 MB
import random

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def quick(sub):
            if len(sub) <= 1:
                return sub

            pivot = random.choice(sub)
            less = [x for x in sub if x < pivot]
            equal = [x for x in sub if x == pivot]
            greater = [x for x in sub if x > pivot]

            return [*quick(less), *equal, *quick(greater)]

        return quick(nums)
```
- 퀵 정렬은 [분할 정복](https://namu.wiki/w/%EB%B6%84%ED%95%A0%20%EC%A0%95%EB%B3%B5%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98) 기법이 아래와 같은 방식으로 응용됨
> - 분할 정복의 부분 배열에서 `pivot`을 선택
> - `pivot`보다 작은 값과 큰 값을 나눠서 재귀호출
> - 작은 값 재귀호출 결과를 `pivot` 앞쪽으로, 큰 값 재귀호출 결과를 `pivot` 뒷쪽으로 두고 배열 조립
- 위 코드에서는 `pivot`을 랜덤하게 뽑아서 그보다 작은값, 같은값, 큰값을 구분한 뒤, 작은값 큰값들을 가진 배열만 재귀호출
- 퀵 정렬 시간복잡도는 일반적으로는 O(N log N)이지만 최악의 경우 O(N²)이 될 수도 있음, 그리고 일반적으로 불안정 정렬이지만 위 코드는 안정 정렬임, 동일한 값을 가진 원소들이 python 리스트 컴프리헨션 문법으로 처리되는데 위치가 안바뀌기 때문임

## in-place 방식 퀵 정렬
```python
# 런타임 597 ms, 메모리 37.9 MB
import random

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def quick(lo, hi):
            if not(lo < hi):
                return

            pivot = nums[random.randint(lo, hi)]
            i, j = lo-1, hi+1
            while True:
                i += 1
                while nums[i] < pivot:
                    i += 1

                j -= 1
                while pivot < nums[j]:
                    j -= 1

                if i >= j:
                    break

                nums[i], nums[j] = nums[j], nums[i]

            quick(lo, j)
            quick(j+1, hi)

        quick(0, len(nums)-1)
        return nums
```
- 보통 퀵 정렬이라 하면 in-place 방식을 이야기하며 변종이 많음, 위 코드의 시간복잡도는 앞서보인 퀵정렬과 동일하나 불안정 정렬임
- 위 코드에서는 `lo`이상, `hi`이하로 주어진 범위를 투 포인터 `i`, `j`가 마주보는 방향으로 진행하면서, `i < j`인 동안 랜덤으로 뽑은 `pivot`을 기준으로 `nums[i] > pivot > nums[j]`가 될 때, `nums[i]`와 `nums[j]`를 스왑
- 이 때, `j`를 기준으로 `lo` ~ `j` 인덱스에는 `pivot`이하의 값이, `j+1` ~ `hi` 인덱스에는 `pivot`이상의 값이 위치하게 됨