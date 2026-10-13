# 기초 영어 문법 (GRAMMAR CORE)

중·고등 내신 대비 문법 교재. 한 원고에서 PDF(인쇄용)와 DOCX(수정용)를 함께 만듭니다.

- 결과물: `dist/기초영어문법.pdf`, `dist/기초영어문법.docx`
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
`**강조**` `==밑줄==` `~~틀림~~` `++고침++` `[[S]]`(성분 라벨)
