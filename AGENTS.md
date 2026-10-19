# 프로젝트 개요

- Astro로 만든 한국어 콘텐츠 중심 블로그다.
- Astro 정적 빌드 결과를 GitHub Pages에 배포한다.
- 프로젝트 변경은 사용자가 요청한 범위에 맞춘다.

# 기술 스택과 명령

- Astro 7, `@astrojs/markdown-remark`, Astro 콘텐츠 컬렉션의 내장 `glob()` 로더를 사용한다.
- CSS 프레임워크는 사용하지 않는다. CSS 초기화에는 `reset-css`를 사용한다.
- Markdown 처리와 rehype 플러그인은 프로젝트 루트의 `astro.config.mjs`에서 설정한다.
- 개발 서버, 빌드, 미리보기 명령은 각각 `npm run dev`, `npm run build`, `npm run preview`다.

# 프로젝트 구조와 라우팅

- `src/layouts/Base.astro`는 공통 HTML 문서, 사이드바 레이아웃, 사이트 메타데이터를 출력한다.
- `src/layouts/Post.astro`는 `Base.astro`를 사용하며 제목, 설명, Markdown 본문을 담는 포스트 레이아웃이다. 홈페이지 Markdown도 이 레이아웃을 사용한다.
- `src/layouts/Header.astro`, `Menu.astro`, `Adsense.astro`, `Footer.astro`는 사이드바의 각 영역을 구성한다. 기존 레이아웃과 메뉴의 태그 구조는 명시적인 요청 없이 바꾸지 않는다.
- 홈페이지 콘텐츠와 메타데이터는 `src/pages/index.md`에서 관리한다.
- `src/data/menu.json` 배열이 사이드바 메뉴 순서와 카테고리별 정렬 방향을 정한다. 항목은 `category`, `title`, `order`를 가지며 `order`는 `asc` 또는 `desc`다.
- `src/pages/category/[slug].astro`는 메뉴에 등록되고 `content/<category>/` 폴더가 있는 카테고리 페이지를 만든다. 포스트는 파일 또는 포스트 폴더 이름의 순번을 오름차순으로 정렬하고 `order: "desc"`이면 역순으로 표시한다. 제목 링크는 `/post/<slug>`를 가리킨다.
- `src/pages/post/[slug].astro`는 메뉴에 등록된 카테고리의 포스트 상세 페이지를 만들고 `src/layouts/Post.astro`를 사용한다. 같은 슬러그가 여러 카테고리에 있으면 경로가 겹칠 수 있으므로 슬러그는 사이트 전체에서 고유하게 유지한다.
- `astro.config.mjs`의 `site`는 `https://znkblog.github.io`다. 주소를 바꾸면 canonical, 구조화 데이터, `src/pages/sitemap.xml.ts`, `public/robots.txt`의 주소도 함께 확인한다.
- 사이트맵은 홈, 메뉴에 등록되고 콘텐츠 폴더가 있는 카테고리, 메뉴에 등록된 카테고리의 포스트를 포함한다. 포스트의 `<lastmod>`는 프론트매터의 `updated` 값이다.
- `public/llms.txt`는 사이트와 콘텐츠 안내 파일이다. 글이나 카테고리를 추가·변경하면 내용과 링크를 실제 사이트에 맞게 갱신한다.
- `public/favicon.svg`, `public/apple-touch-icon.png`, `public/og-image.png`는 사이트 아이콘과 기본 공유 이미지다.

# 콘텐츠 규칙

- 포스트는 프로젝트 루트의 `content/<category>/` 아래에 `[순번]슬러그/index.md` 형식으로 둔다. 이미지 등 포스트에 딸린 리소스도 같은 `[순번]슬러그/` 폴더에 두고 Markdown에서 상대 경로로 참조한다. 기존 `[순번]슬러그.md` 형식도 지원한다.
- 대괄호 안 숫자는 카테고리 목록 정렬용이며 슬러그는 포스트 URL에 사용된다. 포스트 폴더 이름은 `[순번]슬러그` 형식을 따른다.
- `src/content.config.ts`가 `content/`를 읽어 포스트 ID를 `<category>/<slug>`로 만든다. 파일형 포스트는 Markdown 파일명, 폴더형 포스트는 `index.md`를 담은 폴더 이름에서 ID와 순번을 가져온다. 두 형식 이외의 Markdown 경로는 콘텐츠 로딩 오류가 난다.
- 각 포스트 프론트매터에는 `title`, `description`, `updated`, `tags`를 작성한다. `updated`는 `yyyy-mm-dd` 문자열이고 `tags`는 문자열 배열이다.
- 단독 Markdown 주석 `<!--adsense-->`는 `astro.config.mjs`의 rehype 플러그인에서 `adsense-placeholder2` 요소로 바뀐다. 교체할 때는 HTML 문자열을 텍스트 노드로 넣지 말고 HAST 요소 노드로 만든다.

# 스타일 규칙

- 공통 스타일은 `src/styles/global.css`, 페이지별 스타일은 해당 Astro 파일의 `<style>`에 둔다.
- 본문은 NanumSquareRound, `pre`, `code`, `kbd`, `samp`는 D2Coding WOFF2 폰트를 사용한다. 폰트 파일과 라이선스·출처 파일은 `public/fonts/`에 함께 보존한다.
- 반응형 사이드바 동작을 유지한다. 1200px 미만에서는 사이드바가 기본적으로 화면 왼쪽 바깥에 있고 토글 버튼으로 열리며, 본문은 전체 너비를 쓴다.
- 사이드바 메뉴는 헤더와 푸터 사이의 남은 높이를 채우고 자체 스크롤을 유지한다. 스크롤바는 보이지 않게 한다.
- 사이드바는 진한 보라색 계열을 사용한다. CSS 선택자는 `:is()` 대신 일반 선택자로 작성한다.

# 메타데이터와 사이트 검색 정보

- `src/layouts/Base.astro`는 페이지별 props를 받아 제목, 설명, canonical, robots/Googlebot, Open Graph, Twitter, JSON-LD를 출력한다. 기본 공유 이미지와 사이트 공통값은 레이아웃에 정의되어 있다.
- 페이지 메타데이터는 `src/layouts/Post.astro`의 `frontmatter` 또는 `Base.astro`의 `props`로 전달한다. canonical 절대 주소는 `Astro.site`를 기준으로 한다.
- 공통 JSON-LD에는 `WebSite`, `Organization`, `WebPage`가 포함된다. 포스트 상세는 `BlogPosting`, 카테고리는 `CollectionPage`와 순서가 있는 `ItemList`를 전달한다. 화면에 없는 내용이나 확인되지 않은 작성자·게시일·소유 정보를 추가하지 않는다.
- 포스트의 수정일과 주제어는 프론트매터의 `updated`, `tags`를 사용한다. `public/robots.txt`는 전체 크롤링을 허용하고 사이트맵 주소를 안내한다.
- 페이지 제목과 설명, 구조화 데이터는 실제 페이지 내용과 일치시킨다. 새 SEO 메타데이터나 구조화 데이터는 사용자가 요청했거나 작업 범위상 필요한 경우에만 변경한다.

# 작업과 검증

- 요청 범위 밖의 기능 추가, 수정, 리팩터링은 하지 않는다. 요구사항이 모호하고 선택에 따라 결과가 달라지면 구현 전에 확인한다.
- 코드나 설정을 변경한 경우 관련 빌드 또는 검증 명령을 실행한다. 문서만 수정한 경우에는 변경 파일과 diff를 확인한다.
- Markdown 프로세서 설정을 변경하고 개발 서버에 이전 콘텐츠 결과가 남아 있으면 서버를 재시작하고 `npm run dev -- --force`를 실행한다. 마커 변환은 빌드 결과와 브라우저 DOM에서 요소로 생성되는지 확인한다.
- 문서와 코드 주석은 간결한 한국어 평서문으로 작성한다.
