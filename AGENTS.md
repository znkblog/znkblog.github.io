# 프로젝트 개요

- Astro로 만든 한국어 콘텐츠 중심 블로그다.
- Astro 정적 빌드 결과를 GitHub Pages에 배포한다.
- 프로젝트 변경은 사용자가 요청한 범위에 맞춘다.

# 기술 스택과 명령

- Astro 7, `@astrojs/markdown-remark`, Astro 콘텐츠 컬렉션의 내장 `glob()` 로더를 사용한다.
- CSS 프레임워크는 사용하지 않는다. CSS 초기화에는 `reset-css`를 사용한다.
- Markdown 처리, Shiki 코드 테마, rehype 플러그인은 프로젝트 루트의 `astro.config.mjs`에서 설정한다.
- 개발 서버, 빌드, 미리보기 명령은 각각 `npm run dev`, `npm run build`, `npm run preview`다.

# 현재 디렉터리 구조

- `content/`는 실제 Markdown 포스트와 포스트별 이미지 리소스를 보관한다. 현재 공개 카테고리는 `algorithm`, `vibe`다.
- `content/_test/`는 Markdown 동작 확인용 콘텐츠다. 컬렉션, 포스트 경로, 사이트맵에는 포함되지만 `src/data/menu.json`에 등록되지 않아 카테고리 페이지와 사이드바 메뉴에는 나타나지 않는다.
- `src/layouts/`는 공통 문서와 화면 레이아웃을, `src/pages/`는 홈과 정적 경로 생성 코드를 담는다.
- `src/data/menu.json`은 공개 카테고리와 표시 순서 및 포스트 정렬 방향을 관리한다.
- `src/styles/global.css`는 폰트, 공통 색상, 사이드바와 반응형 레이아웃을 관리한다.
- `public/`은 폰트, 아이콘, 공유 이미지, `robots.txt`, `ads.txt`, `llms.txt` 같은 정적 파일을 보관한다.
- `wip/`는 작업 중인 원고를 보관하며 콘텐츠 컬렉션과 빌드 페이지에 포함되지 않는다.
- `dist/`, `.astro/`, `node_modules/`는 생성물 또는 의존성 디렉터리이므로 직접 편집하지 않는다.

# 프로젝트 구조와 라우팅

- `src/layouts/Base.astro`는 공통 HTML 문서, 사이드바 레이아웃, 사이트 메타데이터, GA 태그를 출력한다.
- `src/layouts/Post.astro`는 `Base.astro`를 사용하며 제목, 설명, Markdown 본문을 담는 포스트 레이아웃이다. 홈페이지 Markdown도 이 레이아웃을 사용한다.
- `src/layouts/Header.astro`, `Menu.astro`, `Adsense.astro`, `Footer.astro`는 사이드바의 각 영역을 구성한다. 기존 레이아웃과 메뉴의 태그 구조는 명시적인 요청 없이 바꾸지 않는다.
- 홈페이지 콘텐츠와 메타데이터는 `src/pages/index.md`에서 관리한다.
- `src/pages/404.astro`는 홈과 같은 `Post.astro` 레이아웃을 사용하며 빌드 결과 루트에 GitHub Pages용 `404.html`을 생성한다. canonical은 `/404.html`을 사용하고 검색 결과에 노출되지 않도록 `noindex`를 유지하며 사이트맵에는 넣지 않는다.
- `src/data/menu.json` 배열이 사이드바 메뉴 순서와 카테고리별 정렬 방향을 정한다. 항목은 `category`, `title`, `order`를 가지며 `order`는 `asc` 또는 `desc`다.
- `menu.json`은 사이드바의 `Menu.astro`와 `src/pages/category/[slug].astro`의 카테고리 목록·정렬에 사용한다. 포스트 상세 페이지 생성과 사이트맵의 포스트 포함 여부를 제한하는 용도로 사용하지 않는다.
- `src/pages/post/[slug].astro`는 `posts` 컬렉션의 모든 포스트 상세 경로를 만들고 `src/layouts/Post.astro`로 렌더링한다. `menu.json` 등록 여부는 포스트 생성에 영향을 주지 않는다. 같은 슬러그가 여러 카테고리에 있으면 `/post/<slug>` 경로가 겹치므로 슬러그는 사이트 전체에서 고유하게 유지한다.
- `astro.config.mjs`의 `site`는 `https://znkblog.github.io`다. 주소를 바꾸면 canonical, 구조화 데이터, `src/pages/sitemap.xml.ts`, `public/robots.txt`의 주소도 함께 확인한다.
- `src/pages/sitemap.xml.ts`는 홈, 생성되는 카테고리 페이지, `posts` 컬렉션의 모든 포스트를 사이트맵에 넣는다. 포스트의 `<lastmod>`는 프론트매터의 `updated` 값이다.
- `public/llms.txt`는 사이트 안내 파일이다. 사이트 설명이나 주요 안내 주소를 변경하면 실제 사이트와 일치하도록 갱신한다.
- `public/favicon.svg`, `public/apple-touch-icon.png`, `public/og-image.png`는 사이트 아이콘과 기본 공유 이미지다.

# content 폴더 안의 md 읽어오는 구조

- `src/content.config.ts`의 `posts` 컬렉션이 `glob({ pattern: "**/*.md", base: "./content" })`로 `content/` 아래의 모든 Markdown 파일을 읽는다.
- 지원 경로는 `content/<category>/[순번]<slug>.md`와 `content/<category>/[순번]<slug>/index.md` 두 가지다. 다른 깊이나 이름 형식의 Markdown 경로는 `generateId`에서 오류가 난다.
- 폴더형 포스트의 이미지 등 리소스는 같은 `[순번]<slug>/` 폴더에 두고 Markdown에서 상대 경로로 참조한다.
- `generateId`는 경로의 순번을 제외하고 컬렉션 ID를 `<category>/<slug>`로 만든다. 대괄호 안 숫자는 ID에 포함되지 않으며 카테고리 목록 정렬에만 사용한다.
- 스키마는 `title`, `description`, `updated`, `tags`를 필수로 검증한다. `updated`는 `yyyy-mm-dd` 형식의 문자열이고 `tags`는 문자열 배열이다.
- `src/pages/category/[slug].astro`는 `src/data/menu.json`에 등록된 카테고리만 목록 페이지로 만든다. `src/pages/post/[slug].astro`와 `src/pages/sitemap.xml.ts`는 메뉴 등록 여부와 관계없이 `getCollection("posts")`의 모든 포스트를 사용한다.
- `src/pages/post/[slug].astro`는 선택한 항목을 `render(post)`로 Markdown 컴포넌트로 변환한다.
- 단독 Markdown 주석 `<!--adsense-->`는 `astro.config.mjs`의 rehype 플러그인에서 `div.adsense-placeholder2` HAST 요소로 바뀐다. 교체할 때는 HTML 문자열을 텍스트 노드로 넣지 않는다.

# Category.astro 구조

- `src/pages/category/[slug].astro`는 빌드할 카테고리 경로를 정하는 라우트다. 메뉴 항목의 `category`와 `order`를 검증하고 실제 `content/<category>/` 폴더가 있는 항목만 경로로 만든다.
- 라우트는 포스트의 `filePath`에서 `[순번]`을 읽어 오름차순으로 정렬한 뒤 `order: "desc"`인 카테고리는 역순으로 바꾸고, `title`과 `posts`를 `src/layouts/Category.astro`에 전달한다.
- `src/layouts/Category.astro`는 `Base.astro` 안에 카테고리 제목, 검색 입력, 포스트 목록을 출력하고 `CollectionPage`와 순서가 있는 `ItemList` 구조화 데이터를 만든다.
- 각 포스트 항목은 제목 링크, 설명, 수정일, 태그를 표시한다. 수정일과 태그는 한 행에 놓고 공간이 부족하면 왼쪽 정렬 상태로 줄바꿈한다.
- 제목 링크는 컬렉션 ID에서 카테고리 부분을 제거한 슬러그로 `/post/<slug>`를 가리킨다.
- 검색은 Enter를 눌렀을 때 각 `.post-items`의 전체 텍스트를 대소문자 구분 없이 검사한다. 일치하지 않는 항목은 숨기고 일치 문자열은 `mark.search-highlight`로 강조한다.
- 검색 입력이 공백을 포함해 비게 되면 Enter 입력 없이 모든 항목과 강조 표시를 즉시 복원한다. 한글 조합 중 Enter는 검색을 실행하지 않는다.
- 카테고리 전용 검색창과 목록 스타일은 `src/layouts/Category.astro`의 `<style>`에서 관리한다.

# GA 및 방문자통계

- `src/layouts/Base.astro`의 `<head>`가 Google tag 스크립트를 로드하고 측정 ID `G-MXR6Z4099H`로 GA를 초기화한다. 공통 레이아웃을 쓰는 모든 페이지에 적용된다.
- `src/layouts/Footer.astro`는 사이드바 하단에 GA 활성 사용자 기준 최근 방문자 카드와 7일 그래프를 렌더링한다.
- 브라우저는 같은 출처 경로 `/stat/data/visitors.json`을 `cache: "no-store"`로 요청한다. 브라우저 코드에 원격 `github.io` 절대 URL을 사용하지 않는다.
- 개발 서버에서는 `astro.config.mjs`의 `/stat` 프록시가 요청을 `https://znkblog.github.io`로 전달한다. 배포 환경에서는 현재 사이트의 `/stat/data/visitors.json`을 직접 읽는다.
- 기본 데이터 형식은 `{ data: [{ date, value }] }`다. 정규화 함수는 배열형 응답과 `day`, `dateRange`, `activeUsers`, `users` 등 기존 호환 필드도 처리하고, 날짜순으로 정렬한 마지막 7개 기록만 사용한다.
- 카드 우측 숫자는 7일 합계가 아니라 가장 최근 기록의 활성 사용자 수다. 그래프 접근성 레이블에는 표시 중인 날짜별 사용자 수를 넣는다.
- 데이터가 없거나 요청 및 변환에 실패하면 상태 문구와 접근성 레이블을 갱신한다.
- 방문자 그래프는 사이드바 너비에 맞춰 100%로 표시하고 카드 배경은 투명하게 유지하며 둥근 모서리와 테두리를 두지 않는다. 동적으로 삽입하는 SVG는 자체 크기와 `viewBox`를 가지며 사용자 수는 각 점 위에, 시작·종료 날짜는 좌우 끝에 표시한다.
- Footer 방문자 카드의 세로 크기와 아래쪽 여백은 현재 화면 배치에 맞게 컴팩트하게 유지한다. Footer 아래에 다른 문구를 추가하거나 복원하지 않는다.
- 이 저장소에는 방문자 JSON을 생성하는 코드가 없다. 데이터 생성·배포 방식을 추측하여 추가하지 않는다.

# 스타일 규칙

- 공통 스타일은 `src/styles/global.css`, 페이지별 스타일은 해당 Astro 파일의 `<style>`에 둔다.
- 본문은 NanumSquareRound, `pre`, `code`, `kbd`, `samp`는 D2Coding WOFF2 폰트를 사용한다. 폰트 파일과 라이선스·출처 파일은 `public/fonts/`에 함께 보존한다.
- 반응형 사이드바 동작을 유지한다. 1200px 미만에서는 사이드바가 기본적으로 화면 왼쪽 바깥에 있고 토글 버튼으로 열리며, 본문은 전체 너비를 쓴다.
- 사이드바 메뉴는 헤더와 푸터 사이의 남은 높이를 채우고 자체 스크롤을 유지한다. 스크롤바는 보이지 않게 한다.
- 사이드바는 진한 보라색 계열을 사용한다. CSS 선택자는 `:is()` 대신 일반 선택자로 작성한다.

# 메타데이터와 사이트 검색 정보

- `src/layouts/Base.astro`는 페이지별 props를 받아 제목, 설명, canonical, robots/Googlebot, Open Graph, Twitter, JSON-LD를 출력한다. 기본 공유 이미지와 사이트 공통값은 레이아웃에 정의되어 있다.
- 페이지 메타데이터는 `src/layouts/Post.astro`의 `frontmatter` 또는 `Base.astro`의 `props`로 전달한다. canonical 절대 주소는 `Astro.site`를 기준으로 한다.
- 공통 JSON-LD에는 `WebSite`, `Organization`, `WebPage`가 포함된다. 포스트 상세는 `BlogPosting`, 카테고리는 `CollectionPage`와 순서가 있는 `ItemList`를 추가한다. 화면에 없는 내용이나 확인되지 않은 작성자·게시일·소유 정보를 넣지 않는다.
- 포스트의 수정일과 주제어는 프론트매터의 `updated`, `tags`를 사용한다. `public/robots.txt`는 전체 크롤링을 허용하고 사이트맵 주소를 안내한다.
- 페이지 제목과 설명, 구조화 데이터는 실제 페이지 내용과 일치시킨다. 새 SEO 메타데이터나 구조화 데이터는 사용자가 요청했거나 작업 범위상 필요한 경우에만 변경한다.

# 작업과 검증

- 요청 범위 밖의 기능 추가, 수정, 리팩터링은 하지 않는다. 요구사항이 모호하고 선택에 따라 결과가 달라지면 구현 전에 확인한다.
- 코드나 설정을 변경한 경우 관련 빌드 또는 검증 명령을 실행한다. 문서만 수정한 경우에는 변경 파일과 diff를 확인한다.
- Markdown 프로세서 설정을 변경하고 개발 서버에 이전 콘텐츠 결과가 남아 있으면 서버를 재시작하고 `npm run dev -- --force`를 실행한다. 마커 변환은 빌드 결과와 브라우저 DOM에서 요소로 생성되는지 확인한다.
- 문서와 코드 주석은 간결한 한국어 평서문으로 작성한다.
