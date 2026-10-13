"""교재 콘텐츠 블록 정의 + 인라인 마크업 파서.

인라인 마크업 (본문·표·예문 어디서나 사용 가능)
  **굵게**      → 핵심어 (파트 색상)
  ==형광펜==    → 밑줄/형광 (문제에서 '밑줄 친 부분')
  ~~틀림~~      → 틀린 표현 (빨간 취소선)
  ++맞음++      → 고친 표현 (초록)
  [[S]]          → 문장성분 라벨 칩 (S, V, O, C, I.O, D.O, O.C, M ...)
"""
import re

# ---------- 블록 생성 헬퍼 ----------

def H(text):
    """소단원 제목"""
    return {"t": "h", "text": text}


def P(text):
    """본문 문단"""
    return {"t": "p", "text": text}


def FORMULA(text, sub=None):
    """핵심 공식 박스"""
    return {"t": "formula", "text": text, "sub": sub}


def TABLE(head, rows, widths=None, caption=None, center=None):
    """표. widths: 열 너비 비율 리스트, center: 가운데 정렬할 열 index 집합"""
    return {"t": "table", "head": head, "rows": rows, "widths": widths,
            "caption": caption, "center": set(center or [])}


def EX(items, title=None):
    """예문 리스트: [(영문, 해석), ...]"""
    return {"t": "ex", "items": items, "title": title}


def PARSE(segments, ko=None):
    """문장 구조 분석: [(덩어리, 라벨), ...] 라벨이 None이면 라벨 없음"""
    return {"t": "parse", "segs": segments, "ko": ko}


def TIP(title, lines):
    return {"t": "tip", "title": title, "lines": lines}


def NOTE(title, lines):
    """보충/심화"""
    return {"t": "note", "title": title, "lines": lines}


def WARN(items, title="흔한 실수"):
    """[(틀린 문장, 맞는 문장, 이유), ...]"""
    return {"t": "warn", "title": title, "items": items}


def LIST(items, title=None):
    return {"t": "list", "items": items, "title": title}


def PAGEBREAK():
    return {"t": "pb"}


# ---------- 문제 ----------

def CHECK(steps):
    """steps: [(스텝 이름, 설명, [문제...]), ...]"""
    return {"t": "check", "steps": steps}


def Q(prompt, answer, explain=None, options=None, lines=0):
    """options 있으면 객관식, lines>0 이면 답 쓰는 줄 수"""
    return {"prompt": prompt, "answer": answer, "explain": explain,
            "options": options, "lines": lines}


# ---------- 인라인 마크업 ----------

_TOKEN = re.compile(r"(\*\*.+?\*\*|==.+?==|~~.+?~~|\+\+.+?\+\+|\[\[.+?\]\])")


def tokens(text):
    """'**a** b' → [('b','a'), ('', ' b')] 형태의 (스타일, 문자열) 리스트"""
    out = []
    for part in _TOKEN.split(text):
        if not part:
            continue
        if part.startswith("**"):
            out.append(("b", part[2:-2]))
        elif part.startswith("=="):
            out.append(("hl", part[2:-2]))
        elif part.startswith("~~"):
            out.append(("x", part[2:-2]))
        elif part.startswith("++"):
            out.append(("o", part[2:-2]))
        elif part.startswith("[["):
            out.append(("tag", part[2:-2]))
        else:
            out.append(("", part))
    return out


def plain(text):
    return "".join(s for _, s in tokens(text))
