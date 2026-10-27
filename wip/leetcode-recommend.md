대기업 코테 대비라면 LeetCode 문제를 전부 넓게 풀기보다, 아래처럼 **유형별 대표 문제 40개 정도를 반복해서 푸는 것**을 추천합니다.

다만 한국 대기업 코테는 LeetCode보다 **구현·시뮬레이션·DFS/BFS·완전탐색** 비중이 높은 편이라, LeetCode만 풀면 부족합니다. LeetCode로 알고리즘 패턴을 익히고, 마지막에는 백준·프로그래머스 문제를 섞는 구성이 좋습니다.

## 1단계: 반드시 풀 문제 30개

### 배열·해시

1. [1. Two Sum](https://leetcode.com/problems/two-sum/) — 해시맵
2. [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) — 해시 기준 설계
3. [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) — 집합
4. [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) — 누적 연산
5. [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) — 누적합+해시

특히 560번은 국내 코테에서도 자주 활용되는 누적합 패턴입니다.

### 투 포인터·슬라이딩 윈도우

6. [15. 3Sum](https://leetcode.com/problems/3sum/) — 정렬+투 포인터
7. [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) — 투 포인터 응용
8. [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
9. [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
10. [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

### 스택·큐

11. [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
12. [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) — 모노토닉 스택
13. [155. Min Stack](https://leetcode.com/problems/min-stack/)
14. [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) — 덱

### 이진탐색

15. [704. Binary Search](https://leetcode.com/problems/binary-search/)
16. [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
17. [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) — 매개변수 탐색
18. [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

특히 875번처럼 **정답 범위를 이진탐색하는 문제**는 국내 코테에서도 중요합니다.

### DFS·BFS·그래프

19. [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
20. [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) — 다중 시작점 BFS
21. [133. Clone Graph](https://leetcode.com/problems/clone-graph/)
22. [207. Course Schedule](https://leetcode.com/problems/course-schedule/) — 위상정렬
23. [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
24. [127. Word Ladder](https://leetcode.com/problems/word-ladder/) — 최단거리 BFS

### 백트래킹·완전탐색

25. [78. Subsets](https://leetcode.com/problems/subsets/)
26. [46. Permutations](https://leetcode.com/problems/permutations/)
27. [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
28. [79. Word Search](https://leetcode.com/problems/word-search/)
29. [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
30. [51. N-Queens](https://leetcode.com/problems/n-queens/)

현재 정리 중인 백트래킹 챕터와 연결한다면 `Subsets → Permutations → Combination Sum → Word Search → N-Queens` 순서가 좋습니다.

## 2단계: 합격권을 위한 추가 문제

### 우선순위 큐·그리디

31. [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
32. [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
33. [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
34. [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
35. [55. Jump Game](https://leetcode.com/problems/jump-game/)
36. [134. Gas Station](https://leetcode.com/problems/gas-station/)

### 동적 계획법

37. [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
38. [198. House Robber](https://leetcode.com/problems/house-robber/)
39. [322. Coin Change](https://leetcode.com/problems/coin-change/)
40. [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
41. [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
42. [139. Word Break](https://leetcode.com/problems/word-break/)
43. [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

### 최단경로·Union-Find

44. [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) — 다익스트라
45. [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) — MST
46. [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) — Union-Find
47. [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/) — Union-Find 응용

## 우선순위가 상대적으로 낮은 유형

한국 대기업 코테만 목표로 한다면 다음은 뒤로 미뤄도 됩니다.

- 연결 리스트 세부 기법
- Trie 고난도 문제
- 비트 연산 고난도 문제
- 세그먼트 트리
- LeetCode Hard 수준의 문자열 알고리즘
- 자료구조를 직접 설계하는 인터뷰형 문제

해외 빅테크 인터뷰까지 준비한다면 트리와 연결 리스트 비중을 다시 높여야 합니다.

## 추천 학습 순서

```text
배열·해시
→ 투 포인터·슬라이딩 윈도우
→ 스택·큐
→ 이진탐색
→ DFS·BFS
→ 백트래킹
→ 힙·그리디
→ DP
→ 최단경로·Union-Find
```

한 문제를 풀 때는 다음 기준으로 반복하는 것이 좋습니다.

1. 30분 동안 직접 풀이
2. 못 풀면 해설을 보고 핵심 아이디어만 이해
3. 해설을 닫고 처음부터 다시 작성
4. 3일 뒤 재풀이
5. 2주 뒤 제한시간을 두고 재풀이

입문·중급이라면 공식 **LeetCode 75**, 3개월 이상 준비할 수 있다면 **Top Interview 150**도 좋은 기본 목록입니다. LeetCode는 Top Interview 150을 종합 면접 대비용 150개 고전 문제 목록으로 안내하고 있습니다. [LeetCode](https://leetcode.com/studyplan/top-interview-150/?utm_source=chatgpt.com)

가장 현실적인 조합은 **위 LeetCode 47문제 + 프로그래머스 카카오 기출 + 백준 삼성 SW 역량테스트 기출**입니다. 특히 삼성·CJ 계열 코테까지 생각한다면 LeetCode를 끝낸 뒤 구현과 시뮬레이션 문제를 반드시 별도로 보충해야 합니다.