# znkblog.github.io

개인 블로그용 Astro 프로젝트입니다. 정적 사이트(SSG)로 빌드하여 GitHub Pages에 배포합니다.

## 현재 구성

- Astro `7.3.1`
- Pico CSS `2.1.1` (`@picocss/pico`)
- YAML 파서 `yaml` (`2.9.0`)
- 정적 사이트 출력
- 의존성은 npm으로 관리합니다.
- 기존 루트 `README.md`는 저장소 소개 문서이므로 유지합니다.

## 프로젝트 구조

- `src/components/Base.astro`: 기본 HTML 문서 구조, Pico CSS 전역 import, 공통 헤더/푸터와 `<slot />`을 담당합니다. 기존 링크 구조를 보존합니다.
- `src/components/Post.astro`: `Base.astro`를 감싸는 글 페이지 레이아웃입니다.
- `src/content/index.md`: 홈페이지 콘텐츠이며, 블로그 글 목록과 동적 글 페이지 생성에서 제외합니다.
- `src/content/<category>/`: 블로그 Markdown 글을 둡니다.
- `src/blog.yaml`: 블로그 카테고리 메타데이터입니다.
- `src/pages/index.astro`: `src/content/index.md`를 `Post` 안에서 렌더링합니다.
- `src/pages/blog.astro`: `/blog`의 카테고리별 글 목록입니다.
- `src/pages/blog/[...slug].astro`: 개별 정적 글 페이지를 생성합니다.
- 정적 파일은 `public/`에 둡니다.

## Markdown 콘텐츠 규칙

- 모든 `.md` 파일의 frontmatter는 `title`, `description`, `updated` 필드만 사용합니다.
- 블로그 글 파일명은 `[순번]slug.md` 형식입니다.
  - `[순번]`은 카테고리 목록 정렬용이며 URL에 포함하지 않습니다.
  - `slug`만 사용해 `/blog/slug` 정적 페이지를 생성합니다.
  - `[순번]` 형식이 아닌 파일과 루트 `src/content/index.md`는 개별 글 페이지 생성에서 제외합니다.
  - 모든 글의 slug는 전체 사이트에서 고유해야 합니다. 중복 시 빌드가 실패합니다.

## 카테고리 및 목록 페이지

- `src/blog.yaml`의 각 항목은 `id`, `name`, `order`를 가집니다.
  - `id`: `src/content/` 하위 카테고리 폴더명
  - `name`: `/blog` 화면에 표시할 카테고리명
  - `order`: 파일명 순번의 정렬 방향으로 `asc` 또는 `desc`
- `/blog`에는 YAML에 정의된 카테고리만 표시합니다.
- YAML에 등록된 카테고리의 폴더가 없거나 글이 없으면 안내문을 표시합니다.
- `/blog` 검색은 제목만 대상으로 합니다. Enter 또는 돋보기 버튼으로 실행하며, 일치하지 않는 글을 숨기고 일치하는 제목 부분을 `<mark>`로 강조합니다. 검색어를 비우면 원래 목록을 복원합니다.

## 개발 서버

- `npm run dev`는 `0.0.0.0`에 바인딩하여 실행합니다.
- `astro.config.mjs`의 `server.allowedHosts`에는 개발 서버 접속용 `zzinnykko.iptime.org`가 등록되어 있습니다. 이 설정은 개발/미리보기 서버에만 적용되며 GitHub Pages 정적 배포물에는 영향을 주지 않습니다.

## 명령어

PowerShell 실행 정책으로 `npm`이 차단될 수 있으므로, 이 환경에서는 `npm.cmd`를 사용합니다.

- `npm.cmd run dev`: 개발 서버를 실행합니다.
- `npm.cmd run build`: 정적 프로덕션 빌드를 생성합니다.
- `npm.cmd run preview`: 빌드 결과를 로컬에서 미리 봅니다.

## 작업 지침

- 블로그 콘텐츠와 페이지는 `src/` 아래에 추가합니다.
- Markdown 콘텐츠의 frontmatter 및 파일명 규칙을 지킵니다.
- 변경 후에는 관련되는 경우 `npm.cmd run build`로 빌드를 확인합니다.
