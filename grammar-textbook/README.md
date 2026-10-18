# 문법 공식 (GRAMMAR FORMULA)

중·고등 내신 대비 문법 교재. 한 원고에서 PDF(인쇄용)와 DOCX(수정용)를 함께 만듭니다.

- 결과물: `dist/문법공식_개념편_{학생용,교사용}`, `dist/문법공식_문제편_{학생용,교사용}` (.pdf/.docx) + `문법공식_정답해설.pdf` (별책)
- 개념편: 각 단원 원고에서 STEP UP 이전 핵심만 (기준 문장·단원 연결·학습 목표 제외). 문제편: CHECK-UP + 실전 TEST + 고등 실전 TEST + PART 종합 + 모의고사(3회~ 고등)
- 개념편 단원 첫 쪽·목차에 `▶ 문제편 p.N` 표시 (학생용 문제편 기준 쪽수, 빌드 때 자동 계산)
- 원고: `textbook/content/uNN.py` (단원별), 단원 순서·난이도: `textbook/meta.py`
- 디자인: `assets/style.css` (PDF), `textbook/render_docx.py` (Word)

## 빌드
```
pip install playwright python-docx pypdf reportlab
python3 build.py          # 작성된 전체 단원
python3 build.py 1 2 3    # 일부 단원만
```
글꼴: Pretendard (OFL, `assets/fonts`). Word판은 '맑은 고딕'을 사용합니다.

## 원고 문법
`**강조**` `==밑줄==` `~~틀림~~` `++고침++` `[[S]]`(성분 라벨) `{{정답}}`(필기 빈칸)

## 단원 구성
원본 판서 표 → 필기 포인트(빈칸) → 한 문장 변형하기 → 바로 구별하는 법 → 단원 연결 → STEP UP 심화 → CHECK-UP

## 워터마크 (PDF에 적용됨)
- `assets/del-logo.png` (DEL · Dennis English Laboratory) 로고, 투명 배경 유지
- 모든 페이지 중앙, 가로 420pt(비율 유지), 불투명도 8%
- 사양: `textbook/meta.py`의 `WATERMARK`. 끄려면 `enabled: False`

## 인쇄(제본) 파일
`dist/인쇄용/`
- `*_본문.pdf`: 표지 제외 본문. 목차(1면) → 빈 면 → 본문 1쪽이 오른쪽(홀수 면)에서 시작, 전체 짝수 면
- `*_표지_도련3mm.pdf`: 표지 216 × 303mm (재단 여유 사방 3mm)
- 글꼴은 모두 TrueType으로 임베드 (Pretendard TTF를 시스템 글꼴로 설치해 사용 — 웹폰트로 넣으면 Type 3로 저장됨)
- 좌우 여백 20mm (제본 여백 포함)

## 제본용 파일
`dist/제본용/` (`python3 build.py` 때 자동 생성)
- 책마다 `N_…_본문.pdf` + `N_…_표지.pdf`(펼침: 뒤표지 | 책등 | 앞표지, 도련 3mm) + `제본_사양서.txt`
- 64쪽 이하 → 중철(4의 배수로 빈 면 채움), 넘으면 무선(책등 자동 계산)
- 종이 두께·중철 기준: `textbook/meta.py`의 `BIND`
