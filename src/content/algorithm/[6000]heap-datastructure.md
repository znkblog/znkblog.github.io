---
title: "힙 (Heap) 자료구조"
description: "이진트리를 배열과 같은 연속된 선형 데이터셋으로 표현하는 힙 자료구조 소개"
updated: "2026-09-16"
---

## 힙 자료구조

이진트리의 일종임, [나무위키](https://namu.wiki/w/%ED%9E%99%20%ED%8A%B8%EB%A6%AC)를 보면 바로 보이는 그림이 힙 자료구조인데, 재밌는 것은 개념은 이진트리지만 배열과 같은 선형 데이터셋으로 이를 표현할 수 있음,

이진트리는 자식 노드가 최대 2 개 달려있는 트리로, 모든 이진트리가 힙 자료구조가 될 수 있는 것은 아님, 중간에 자식노드가 불완전하게 붙어있으면 안되는 **완전 이진트리 구조** 이어야 하며, 일부 제약이 추가 됨, 아래와 같음,

> - 마지막 레벨을 제외한 모든 레벨의 노드들은 2 개 노드를 모두 가지고 있어야 함,
> - 데이터를 채울 때는 항상 제일 왼쪽 노드부터 차례로 채워져야 함,
> - 최소 힙의 경우, 부모노드는 자식노드보다 항상 작거나 같은 값을 유지해야 함, (최대 힙의 경우는 반대)

위 조건을 만족할 경우, 이진트리는 힙 자료구조가 되며, 배열로 표현할 수 있음, 배열로 표현했을 때의 이점은 탐색의 속도가 매우 빠르다는 것임,

예를들어 위와 같은 조건을 만족하는 힙 자료구조는, 간단한 산술식으로 부모, 자식 간의 크기 순서를 유지할 수 있으며, 최대값이나 최소값을 찾는다고 하면, 루트의 값을 가져오기만 하면 되므로 O(1) 속도 구현이 가능함, (부모노드는 자식노드보다 무조건 작거나 같은 값이어야 하므로, 루트는 전체 데이터 중 가장 작은 값을 가질 수밖에 없음)

힙 자료구조는 보통 우선순위 큐 구현이나 정렬에 사용됨,

## 구조

배열로 표현 가능하다는 것은, 메모리에 노드를 만들고 이를 연결하는 것이 아니라, 배열의 인덱스 관계로 노드와 노드 연결을 대신할 수 있다는 의미임, 부모노드를 p, 자식노드를 c1, c2 라고 했을 때, 이들의 인덱스는 아래와 같은 관계를 가짐,

```plaintext
c1 = p * 2 + 1
c2 = p * 2 + 2
p = (c1 - 1) // 2
p = (c2 - 1) // 2
```

예를들어, 인덱스에 해당 인덱스 번호가 데이터로 들어있는 힙 자료구조를 생각했을 경우, 아래와 같게 나올 수 있는데, 위 수식이 적용되는지는 직접 계산해 보면 됨,

```plaintext
                   [0]
                    |
         +----------+----------+
         |                     |
        [1]                   [2]
         |                     |
    +----+----+           +----+----+
    |         |           |         |
   [3]       [4]         [5]       [6]
    |         |           |         |
 +--+--+   +--+--+     +--+--+   +--+--+
 |     |   |     |     |     |
[7]   [8] [9]  [10]  [11]  [12]   ....
```

## 코드 구현

최소 힙을 예시로 함, 최대 힙을 구하고자 한다면 나중에 부등호 방향만 반대로 하면 됨,

heap 자료구조를 A 라 하고, 힙 자료구조에 데이터를 하나씩 넣는 heappush, 데이터를 하나씩 빼내는 heappop 을 구현하면 됨,

데이터를 heappush 하는 경우는...

> - A 의 가장 뒤 인덱스 c 에 데이터 대입,
> - c 의 부모 인덱스 p 를 공식 (c - 1) // 2 로 구함,
> - c 가 최상위 루트가 아니면서, A[p] > A[c] 이면 스왑, c 를 p 로 업데이트하고 위 단계 반복,
> - 아니라면 실행 종료,

heappop 하는 경우는...

> - A 의 루트 값을 따로 저장해둠,
> - A 의 제일 마지막 원소값을 루트로 이동하고 마지막 인덱스 삭제,
> - A 에 원소가 남아있다면 0 인덱스를 p 로 보고, 공식 사용하여 두 자식 인덱스를 계산 해 둠, c1 = p * 2 + 1, c2 = p * 2 + 2,
> - 만일 c2 가 A 인덱스 범위 안에 있으면서, A[c1] > A[c2] 라면 c = c2, 아니라면 c = c1 이라 함,
> - c 가 A 인덱스 범위 안에 들어오면서, A[p] > A[c] 이면 스왑, p 를 c 로 업데이트하고 다시 반복,
> - 아니라면 따로 저장해뒀던 값을 리턴하고 종료

## leetcode 912. Sort an Array

[https://leetcode.com/problems/sort-an-array/](https://leetcode.com/problems/sort-an-array/)

주어진 nums 리스트를 정렬하는 문제, 여기서는 힙 자료구조를 사용하는 힙 정렬로 풀어 봄,

힙 정렬은 시간복잡도 O(nlogn) 이며, 불안정 정렬임,

python 코드로 풀어보면 아래와 같음,

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return heapSort(nums)

def heapSort(nums: List[int]) -> List[int]:
    # heappush
    heap = []
    for x in nums:
        heap.append(x)
        c = len(heap) - 1
        p = (c - 1) // 2

        while c > 0 and heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            c = p
            p = (c - 1) // 2
    
    # heappop
    a = []
    while heap:
        root = heap[0]
        last = heap.pop()

        if heap:
            heap[0] = last
            p = 0
            while True:
                c1, c2 = p*2 + 1, p*2 + 2
                c = c2 if c2 < len(heap) and heap[c1] > heap[c2] else c1 

                if c < len(heap) and heap[p] > heap[c]:
                    heap[p], heap[c] = heap[c], heap[p]
                    p = c
                else:
                    break
            
        a.append(root)

    return a
```

heappush 와 heappop 을 동시에 하나의 함수에 구현하였음, nums 를 heap 이라는 힙 자료구조로 변환한 다음, 하나씩 팝 하는 구조임,

그리고 예를들어 `[(3, "A"), (1, "B"), (3, "C")]` 가 있을 때, 튜플의 정수를 기준으로 최소힙 자료구조로 만들면, `[(1, "B"), (3, "A"), (3, "C")]` 가 됨,

여기서 heappop 이 적용되면, 제일 먼저 `(1, "B")` 를 얻을 수 있고, 힙 자료구조는 `[(3, "C"), (3, "A")]` 가 되며, 다음 heappop 에는 `(3, "C")` 가 나오게 됨, 제일 뒤에 있던 값이 0 번 인덱스로 오는 heappop 과정 때문에, 동일한 크기의 원소 순서가 뒤바뀔 수 있음, 즉 불안정 정렬임,

참고로 python 은 빌트인 라이브러리로 힙 자료구조 함수를 지원함, 아래는 이를 이용한 풀이임,

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return heapSort(nums)

def heapSort(nums: List[int]) -> List[int]:
    heapq.heapify(nums)
    
    a = []
    while nums:
        x = heapq.heappop(nums)
        a.append(x)

    return a
```

본래라면 heapq 라이브러리를 임포트해야 하지만, leetcode 에서는 임포트 없이 사용 가능함,

heapq.heapify 함수는 어떤 리스트를 힙 자료구조로 바꿔주는 함수임, 여기에 heapq.heappop 을 적용하여 리턴함, 물론 heapq.heappush 함수도 라이브러리에 있으나 굳이 사용할 필요는 없음,

다만 위 풀이는 leetcode 가 치팅이라고 판단하는지 풀리지는 않고 에러가 발생함,