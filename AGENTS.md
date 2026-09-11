# znkblog.github.io

개인 블로그용 Astro 프로젝트입니다. 정적 사이트(SSG)로 빌드하여 GitHub Pages에 배포합니다.

## 현재 구성

- Astro `7.3.1`
- Pico CSS `2.1.1` (`@picocss/pico`)
- YAML 파서 `yaml` (`2.9.0`)
- Astro sitemap 통합 `@astrojs/sitemap`
- 의존성은 npm으로 관리합니다.
- 기존 루트 `README.md`는 저장소 소개 문서이므로 유지합니다.

## 프로젝트 구조

- `src/components/Base.astro`: 기본 HTML 문서 구조, Pico CSS 전역 import, 공통 헤더/푸터와 `<slot />`을 담당합니다. 페이지별 title·description·canonical·Open Graph 메타데이터, favicon, 게시글용 JSON-LD도 이 컴포넌트에서 처리합니다. 사용자가 수정한 내비게이션 링크는 보존합니다.
- `src/components/Post.astro`: `title`, `description`, `updated`를 `Astro.props`로 받아 slot을 렌더링하는 글 레이아웃입니다.
- `src/content/index.md`: 홈페이지 콘텐츠이며, 블로그 글 목록과 개별 글 경로 생성에서 제외합니다.
- `src/content/<category>/`: 블로그 Markdown 글을 둡니다.
- `src/blog.yaml`: 블로그 카테고리 메타데이터입니다.
- `src/pages/index.astro`: `src/content/index.md`를 import하고 frontmatter를 `Post`에 전달합니다.
- `src/pages/blog.astro`: `/blog`의 카테고리 안내문, 접이식 카테고리별 글 목록, 제목 검색·강조 기능을 담당합니다.
- `src/pages/blog/[...slug].astro`: 개별 정적 글 페이지를 생성합니다.
- `astro.config.mjs`: 사이트 주소를 설정하고 `@astrojs/sitemap`으로 빌드 시 sitemap을 생성합니다.
- `.github/workflows/deploy-pages.yml`: 수동 실행하는 GitHub Pages 빌드·배포 워크플로입니다.
- `public/favicon.svg`, `public/favicon.ico`: ZNK 로고 favicon입니다.
- `public/robots.txt`: 검색엔진 크롤링 허용 및 배포 sitemap 주소를 안내합니다.
- `under-construction/`: 아직 공개하지 않는 Markdown 초안입니다. `src/content/` 밖에 두어 Astro 빌드와 블로그 목록에서 제외합니다.
- 정적 파일은 `public/`에 둡니다.
- Astro 컴포넌트 스타일은 일반 CSS를 사용하며, Sass·SCSS 의존성과 `lang="scss"` 스타일 태그를 추가하지 않습니다.

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
- 현재 공개 카테고리는 `vibe`(Vibe 코딩, `desc`)와 `algorithm`(알고리즘 스터디, `asc`)입니다.
- `/blog`에는 YAML에 정의된 카테고리만 표시합니다.
- YAML에 등록된 카테고리의 폴더가 없거나 글이 없으면 안내문을 표시합니다.
- 카테고리는 처음에 접힌 상태이며, 카테고리 제목을 클릭해 펼치거나 접습니다. 접힘·펼침 표식 CSS는 현재 주석 처리되어 있어 표시하지 않습니다.
- `/blog` 검색은 제목만 대상으로 합니다. Enter 또는 돋보기 버튼으로 실행하며, 일치하지 않는 글을 숨기고 일치하는 제목 부분을 `<mark>`로 강조합니다. 검색 결과가 있는 카테고리는 자동으로 펼치며, 검색어를 비우면 전체 목록을 다시 접습니다.

## GitHub Pages 배포

- `.github/workflows/deploy-pages.yml`은 `workflow_dispatch`로 수동 실행할 때만 동작합니다.
- 워크플로는 Node.js `24`에서 `npm i`, `npm run build`를 실행한 뒤 생성된 `dist/` 디렉터리를 공식 GitHub Pages 액션으로 배포합니다.
- `astro.config.mjs`의 `site`는 `https://znkblog.github.io`이며, `npm.cmd run build` 시 `dist/sitemap-index.xml`과 sitemap 파일이 생성됩니다.
- `robots.txt`는 배포된 `https://znkblog.github.io/sitemap-index.xml`을 sitemap 주소로 사용합니다.
- sitemap은 개발 서버(`npm.cmd run dev`)에서는 생성되지 않으므로 개발 중 `/sitemap-index.xml`이 404여도 정상입니다. 배포 산출물은 `npm.cmd run preview`로 확인합니다.
- 저장소의 GitHub Pages 설정에서 배포 원본으로 **GitHub Actions**를 선택합니다.

## 개발 서버

- `npm run dev`는 Astro의 기본값인 `localhost`에만 바인딩하여 실행합니다. 외부 네트워크에서는 개발 서버에 접속할 수 없습니다.
- `astro.config.mjs`에는 외부 호스트를 허용하는 개발 서버 설정을 두지 않습니다.

## 명령어

PowerShell 실행 정책으로 `npm`이 차단될 수 있으므로, 이 환경에서는 `npm.cmd`를 사용합니다.

- `npm.cmd run dev`
- `npm.cmd run build`
- `npm.cmd run preview`

관련 변경 후에는 `npm.cmd run build`로 빌드를 확인합니다.

## SEO 및 광고 준비

- 공개 페이지에는 페이지별 title, description, canonical URL, Open Graph 메타데이터가 적용됩니다.
- 개별 게시글에는 `BlogPosting` JSON-LD가 적용됩니다.
- sitemap과 robots.txt는 빌드·배포 결과에 포함됩니다.
- AdSense 계정 승인 전에는 임의의 광고 코드나 빈 광고 영역을 추가하지 않습니다. 승인 후 발급된 `client`와 `slot` 값을 사용해 본문 흐름을 해치지 않는 위치에 추가합니다.
- 광고 승인과 별개로 개인정보처리방침, 운영자 소개, 문의 방법, 충분한 독창적 콘텐츠를 준비하는 것이 좋습니다.
