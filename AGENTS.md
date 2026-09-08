# znkblog.github.io

개인 블로그용 Astro 프로젝트입니다. 현재는 Astro의 minimal 템플릿을 기반으로 합니다.

## 현재 구성

- Astro `7.3.1`
- 정적 사이트 출력
- 의존성은 npm으로 관리합니다.
- 기존 루트 `README.md`는 저장소 소개 문서이므로 유지합니다.

## 명령어

- `npm run dev`: 개발 서버를 `0.0.0.0`에 바인딩하여 실행합니다.
- `npm run build`: 정적 프로덕션 빌드를 생성합니다.
- `npm run preview`: 빌드 결과를 로컬에서 미리 봅니다.

## 작업 지침

- 블로그 콘텐츠와 페이지는 `src/` 아래에 추가합니다.
- 정적 파일은 `public/`에 둡니다.
- 변경 후에는 관련되는 경우 `npm run build`로 빌드를 확인합니다.
