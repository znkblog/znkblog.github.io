---
title: "마크다운 요소 둘러보기"
description: "블로그에서 사용하는 표준 마크다운과 GFM 문법을 확인하는 테스트 포스트."
updated: "2026-10-18"
tags: ["마크다운", "테스트", "GFM"]
---

# 제목 1

이 문서는 **굵은 글씨**, *기울임*, ~~취소선~~, 그리고 `인라인 코드`를 보여줘. 링크는 [Astro 공식 사이트](https://astro.build/)로 연결돼.

<!--adsense-->

## 제목 2

일반 문단은 여러 문장으로 구성할 수 있어. 줄을 바꿔도 같은 문단이면
렌더링 결과에서는 한 문단으로 이어져.

### 제목 3

#### 제목 4

##### 제목 5

###### 제목 6

## 인용문

> 인용문은 본문과 구분되어 표시돼.
>
> 여러 문단이나
> > 중첩된 인용문도 작성할 수 있어.

## 목록

- 순서 없는 목록 항목
- 또 다른 항목
  - 들여쓴 하위 항목
  - **서식이 포함된** 항목

1. 순서 있는 첫 번째 항목
2. 두 번째 항목
   1. 하위 순서 항목
   2. 다음 하위 항목

## 작업 목록

- [x] 완료한 작업
- [ ] 아직 남은 작업

## 코드 블록

```ts
type Post = {
  title: string;
  published: boolean;
};

const post: Post = { title: "예제 포스트", published: true };
console.log(post.title);
```

## 표

| 문법 | 예시 | 설명 |
| --- | --- | --- |
| 굵게 | `**텍스트**` | 강조 |
| 기울임 | `*텍스트*` | 기울임꼴 |
| 취소선 | `~~텍스트~~` | GFM 확장 |

## 이미지와 구분선

<svg role="img" aria-label="마크다운 이미지 예시" viewBox="0 0 640 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="640" height="180" rx="16" fill="#e8e3d9" />
  <circle cx="95" cy="90" r="42" fill="#bd7955" />
  <path d="M78 93l12 12 24-30" fill="none" stroke="#fffdf8" stroke-linecap="round" stroke-linejoin="round" stroke-width="8" />
  <text x="160" y="102" fill="#20343a" font-family="sans-serif" font-size="30">Inline SVG image example</text>
</svg>

---

## 인라인 HTML 요소

HTML 태그도 마크다운 안에 넣을 수 있어: <mark>강조 표시</mark>, H<sub>2</sub>O, x<sup>2</sup>, <abbr title="HyperText Markup Language">HTML</abbr>, <kbd>Ctrl</kbd> + <kbd>C</kbd>.

<details>
  <summary>눌러서 펼쳐 보는 내용</summary>
  <p>details와 summary 요소가 마크다운 본문에서도 동작하는지 확인해.</p>
</details>
