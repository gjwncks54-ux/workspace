# 기초 영어 문법 (GRAMMAR CORE)

중·고등 내신 대비 문법 교재. 한 원고에서 PDF(인쇄용)와 DOCX(수정용)를 함께 만듭니다.

- 결과물: `dist/기초영어문법_학생용.pdf/.docx` (필기 빈칸), `dist/기초영어문법_교사용.pdf/.docx` (빈칸 정답 표시)
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

## 워터마크 (기억용, 현재 미적용)
- `assets/del-logo.png` (DEL · Dennis English Laboratory) 로고, 투명 배경 유지
- 모든 페이지 중앙, 가로 420pt(비율 유지), 불투명도 8%
- 사양: `textbook/meta.py`의 `WATERMARK`. 현재는 선생님이 직접 삽입하므로 `enabled: False`
