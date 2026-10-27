---
title: "chatgpt가 추천한 코딩테스트 합격 위해 풀어봐야할 leetcode 문제"
description: "대기업 코딩테스트 유형 연습을 위해서 반드시 그리고 추가적으로 풀어볼만한 leetcode 문제 예시"
updated: "2026-10-27"
tags: ["algorithm", "coding_test", "leetcode"]
---

- chatgpt에 **"대기업 코딩테스트 대비하기 위해 풀어봐야할 leetcode 문제를 추천해줘"**라고 요청해서 받은 리스트임
- chatgpt는 폭넓게 여러개 풀어보기 보다는 유형별 대표문제를 반복해서 풀어볼 것을 권장하였음
- leetcode만으로는 부족하며 이후에는 프로그래머스나 백준 사이트도 보충도 필요하다고 함 (다른 사이트 문제들도 기회가 되면 풀이를 포스팅할 예정)
- 아래 리스트에서 링크가 활성화된 문제들은 본인의 풀이 포스팅으로 연결이 됨(비활성화된 문제들은 아직 풀기 전이나 포스팅이 없는 문제들임), 풀이 포스팅에서 leetcode 문제 연결 및 다양한 풀이법을 소개하고자 함

## 1단계: 반드시 풀 문제 30개
### 배열·해시
- [1. Two Sum](/post/leetcode-two-sum) — 해시맵
- 49. Group Anagrams — 해시 기준 설계
- 128. Longest Consecutive Sequence — 집합
- 238. Product of Array Except Self — 누적 연산
- 560. Subarray Sum Equals K — 누적합+해시

### 투 포인터·슬라이딩 윈도우
- 15. 3Sum — 정렬+투 포인터
- 42. Trapping Rain Water — 투 포인터 응용
- 121. Best Time to Buy and Sell Stock
- 3. Longest Substring Without Repeating Characters
- 209. Minimum Size Subarray Sum

### 스택·큐
- 20. Valid Parentheses
- 739. Daily Temperatures — 모노토닉 스택
- 155. Min Stack
- 239. Sliding Window Maximum — 덱

### 이진탐색
- 704. Binary Search
- 33. Search in Rotated Sorted Array
- 875. Koko Eating Bananas — 매개변수 탐색
- 153. Find Minimum in Rotated Sorted Array

### DFS·BFS·그래프
- 200. Number of Islands
- [994. Rotting Oranges](post/leetcode-rotting-oranges) — 다중 시작점 BFS
- 133. Clone Graph
- 207. Course Schedule — 위상정렬
- 417. Pacific Atlantic Water Flow
- 127. Word Ladder — 최단거리 BFS

### 백트래킹·완전탐색
- 78. Subsets
- 46. Permutations
- 39. Combination Sum
- 79. Word Search
- 22. Generate Parentheses
- 51. N-Queens

## 2단계: 합격권을 위한 추가 문제
### 우선순위 큐·그리디
- 215. Kth Largest Element in an Array
- 347. Top K Frequent Elements
- 973. K Closest Points to Origin
- 56. Merge Intervals
- 55. Jump Game
- 134. Gas Station

### 동적 계획법
- [70. Climbing Stairs](post/leetcode-climbing-stairs)
- 198. House Robber
- 322. Coin Change
- 300. Longest Increasing Subsequence
- 1143. Longest Common Subsequence
- 139. Word Break
- 416. Partition Equal Subset Sum

### 최단경로·Union-Find
- 743. Network Delay Time — 다익스트라
- 1584. Min Cost to Connect All Points — MST
- 684. Redundant Connection — Union-Find
- 721. Accounts Merge — Union-Find 응용

## chatgpt 추천은 아니지만 따로 풀어본 것들
- [53. Maximum Subarray](post/leetcode-maximum-subarray) - 분할 정복, 동적 계획법