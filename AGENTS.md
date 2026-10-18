# 프로젝트 개요

- 이 프로젝트는 Astro로 만든 한국어 콘텐츠 중심 블로그다.
- 결과물은 정적 사이트이며 GitHub Pages 배포를 전제로 한다.
- 프로젝트 변경은 사용자가 명확하게 요청한 범위에서 수행한다.

# 기술 스택

- Astro 7 이상을 사용한다.
- 별도의 CSS 프레임워크는 사용하지 않는다.
- CSS 초기화에는 npm 패키지 `reset-css`를 사용한다.
- 포스트는 Astro 콘텐츠 컬렉션과 내장 `glob()` 로더로 불러온다.
- 개발 서버는 `npm run dev`, 정적 빌드는 `npm run build`, 빌드 결과 미리보기는 `npm run preview`로 실행한다.

# 사이트 구조와 라우팅

- `src/components/Base.astro`는 페이지에서 공통으로 사용하는 HTML 기반 레이아웃이다.
- `src/data/menu.json`은 사이드바의 카테고리 메뉴와 포스트 정렬 방향을 관리한다.
- 메뉴 항목은 `category`, `title`, `order`를 가진다. `order` 값은 `asc` 또는 `desc`이며 배열 순서는 메뉴 표시 순서다.
- `src/pages/category/[slug].astro`는 메뉴에 등록되어 있고 `content/<category>/` 폴더가 존재하는 카테고리 페이지를 `/category/<category>` 주소로 정적으로 생성한다.
- 카테고리 포스트는 파일명에 지정한 순번을 기준으로 메뉴의 `order` 방향에 맞게 표시한다. 메뉴에 없는 콘텐츠 카테고리는 카테고리 페이지에서 제외한다.
- `src/pages/post/[slug].astro`는 메뉴에 등록된 카테고리의 포스트 상세 페이지를 `/post/<slug>` 주소로 정적으로 생성한다.
- 카테고리 목록의 포스트 제목 링크는 해당 `/post/<slug>` 페이지를 가리킨다.
- `astro.config.mjs`의 `site`는 `https://znkblog.github.io`로 설정한다. canonical URL, 구조화 데이터, robots 및 sitemap의 도메인은 이 사이트 주소와 일치시킨다.
- `src/pages/sitemap.xml.ts`는 홈, 실제 생성되는 카테고리 페이지, 메뉴에 등록된 카테고리의 포스트 페이지 URL을 sitemap으로 만든다. `public/robots.txt`는 크롤링을 허용하고 sitemap URL을 알린다.

# 콘텐츠 규칙

- 포스트는 프로젝트 루트의 `content/<category>/` 아래에 둔다.
- 포스트 파일명은 `[순번]슬러그.md` 형식이다. 대괄호 안 숫자는 정렬용 순번이며 뒤의 문자열은 포스트 슬러그다.
- 포스트 프론트매터에는 `title`, `description`, `updated`, `tags`를 모두 작성한다.
- `updated`는 `yyyy-mm-dd` 형식의 문자열이다.
- `tags`는 `["태그1", "태그2"]` 형식의 인라인 배열이다.
- `src/content.config.ts`는 프로젝트 루트의 `content/`를 읽고 포스트 ID를 `<category>/<slug>` 형식으로 만든다.

# 디자인 규칙

- 공통 스타일은 `src/styles/global.css`에 작성하고 `Base.astro`에서 불러온다.
- 페이지에 한정된 스타일은 해당 Astro 파일의 `<style>`에 작성한다.
- 레이아웃과 메뉴의 기존 태그 구조는 명시적인 요청이 없는 한 변경하지 않는다.
- 사이드바와 본문은 반응형으로 유지한다. 화면 폭 1200px 미만에서는 사이드바를 기본적으로 왼쪽 화면 밖에 두고 토글 버튼으로 열고 닫으며, 본문은 화면 너비를 모두 사용한다.
- 사이드바 메뉴 영역은 헤더와 푸터 사이의 남은 높이를 채운다. 스크롤 동작은 유지하고 스크롤바는 보이지 않게 한다.
- 사이드바는 진한 보라색 계열을 사용한다.
- CSS 선택자에는 `:is()` 대신 일반 선택자를 사용한다.

# 검색엔진 및 생성형 검색 최적화

- `src/components/Base.astro`에서 문서 제목과 설명, canonical, robots, Googlebot, Open Graph, Twitter 카드, JSON-LD를 공통으로 출력한다.
- 페이지별 제목, 설명, canonical URL, 페이지 유형, 언어·로케일, 공유 이미지, 구조화 데이터는 `Base.astro`의 `props`로 전달한다. 생략한 값은 공통 기본값을 사용한다.
- canonical과 구조화 데이터의 절대 URL은 `astro.config.mjs`에 설정한 `site`를 기준으로 만든다. 홈은 `/`, 카테고리는 `/category/<category>/`, 포스트는 `/post/<slug>` 주소를 사용한다.
- 사이트와 색인 대상 페이지는 한국어로 표시하고 robots 색인을 기본 허용한다. 색인에서 제외할 페이지에만 `noindex`를 지정한다.
- 기본 JSON-LD에는 `WebSite`, `Organization`, `WebPage`를 사용한다. 포스트 상세에는 `BlogPosting`, 카테고리 페이지에는 `CollectionPage`와 포스트 순서가 포함된 `ItemList`를 추가한다.
- `og:image`와 Twitter 이미지 메타데이터는 실제로 존재하는 공유 이미지를 해당 페이지에 전달한 경우에만 출력한다. 이미지가 없으면 이미지 카드 유형을 가장하지 않는다.
- 작성자, 게시일, 사이트 소유 정보 등 확인할 수 없는 사실을 메타데이터나 구조화 데이터에 만들어 넣지 않는다. 포스트 수정일과 주제어는 프론트매터의 `updated`, `tags`를 사용한다.
- `src/pages/sitemap.xml.ts`는 홈, 메뉴에 등록되고 콘텐츠 폴더가 존재하는 카테고리, 해당 카테고리의 포스트만 사이트맵에 포함한다. 포스트의 `<lastmod>`는 프론트매터 `updated` 값으로 만든다.
- `public/robots.txt`는 사이트 크롤링을 허용하고 `https://znkblog.github.io/sitemap.xml`을 알린다. 사이트 주소를 변경하면 Astro `site`, robots, 사이트맵의 URL도 함께 갱신한다.
- GEO를 위해 페이지별 제목과 설명은 페이지의 실제 내용과 일치하도록 작성하고, 구조화 데이터는 화면에 표시되는 내용과 일치시킨다. 키워드 나열이나 근거 없는 표현은 추가하지 않는다.

# 작업 및 검증 규칙

- 요청 범위 밖의 기능 추가, 수정, 리팩터링은 하지 않는다.
- 모호하거나 여러 선택지가 있는 요구사항은 구현 전에 확인한다.
- SEO/GEO 메타데이터와 JSON-LD는 명시적으로 요청된 경우에만 추가한다.
- 변경 후에는 관련 빌드나 검증 명령으로 결과를 확인한다.
- 이 문서와 코드 주석은 간결한 한국어 평서문으로 작성한다.
