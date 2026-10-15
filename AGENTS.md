# 작업 지침

- Astro 7 이상을 사용해 블로그 또는 홈페이지를 정적 사이트로 만들고 GitHub Pages 배포를 전제로 한다.
- 별도의 CSS 프레임워크는 사용하지 않고, Eric Meyer reset CSS는 npm 패키지 `reset-css`를 사용한다.
- `src/components/Base.astro`를 공통 HTML 기반 레이아웃으로 사용한다. SEO/GEO 메타데이터와 JSON-LD는 명시적으로 요청된 경우에만 추가한다.
- 포스트는 프로젝트 루트 `content/<category>/`에 둔다. 파일명은 `[순번]슬러그.md` 형식을 따르고, 대괄호 순번은 정렬용이며 대괄호 뒤 문자열은 URL 슬러그로 사용한다.
- 모든 포스트 프론트매터에는 `title`, `description`, `updated`, `tags`를 둔다. `updated`는 `yyyy-mm-dd` 형식의 문자열로, `tags`는 `["태그1", "태그2"]` 형태의 인라인 배열로 작성한다.
- `src/data/menu.json`에서 카테고리 메뉴와 포스트 정렬 방향을 관리한다. 메뉴 배열 순서가 표시 순서이며 각 항목은 `category`, `title`, `order`(`asc` 또는 `desc`)를 가진다.
- 카테고리 페이지는 `src/pages/category/[slug].astro`에서 정적으로 생성한다. 메뉴에 등록되고 `content/<category>/` 폴더가 실제로 있는 카테고리만 `/category/<category>` 페이지로 만들며, 설정에 없는 콘텐츠 폴더는 무시한다. 포스트는 파일명 순번 기준으로 `order` 방향에 맞게 표시한다.
- `src/content.config.ts`에서 Astro 내장 `glob()` 로더로 프로젝트 루트의 `content/`를 읽고, 포스트 ID는 `<category>/<slug>` 형태로 만든다.
- `Base.astro`의 사이드바 메뉴는 헤더와 푸터 사이의 남은 높이를 채우고, 스크롤바는 보이지 않게 하되 스크롤 동작은 유지한다. 화면 폭 1200px 미만에서는 사이드바를 기본적으로 화면 왼쪽 밖에 두고 토글 버튼으로 전환하며, 본문 너비는 100%로 한다. CSS 선택자는 `:is()` 대신 일반 선택자를 사용한다.
- 사용자가 명확하게 지시한 작업만 수행한다. 모호하거나 선택이 필요한 사항은 임의로 결정하지 말고 먼저 확인한다.
- 요청 범위 밖의 수정, 기능 추가, 리팩터링은 하지 않는다.
- 사용자가 편집 중인 HTML은 명시적 요청 없이 수정하지 않는다.
- 이 파일의 지침은 경어 없이 간결한 한국어로 작성한다.