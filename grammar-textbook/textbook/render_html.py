"""콘텐츠 → HTML 문자열"""
import re
from html import escape
from pathlib import Path

from textbook.blocks import blanks, tokens
from textbook.meta import BOOK, PARTS

ROOT = Path(__file__).resolve().parent.parent
CSS = (ROOT / "assets" / "style.css").read_text(encoding="utf-8")
FONT_DIR = (ROOT / "assets" / "fonts").as_uri()

CIRCLED = "①②③④⑤"
CIRC_RE = re.compile("[\u24d0-\u24e9]")  # ⓐ~ⓩ: 본문 글꼴에 없어 CSS 원문자로 그린다
MODE = {"teacher": False, "book": ""}  # 학생용/교사용, 개념편/문제편


def blank_len(s):
    return max(3.0, sum(1.0 if ord(ch) > 0x2000 else 0.55 for ch in s) + 1.5)

TAG_CLASS = {"S": "s", "V": "v", "O": "o", "C": "c", "I.O": "o", "D.O": "o2",
             "O.C": "c", "M": "m", "S'": "s", "V'": "v"}


def inline(text):
    out = []
    for style, s in tokens(str(text)):
        s = escape(s).replace("\n", "<br>")
        s = CIRC_RE.sub(lambda m: f'<span class="circ">{chr(ord(m.group()) - 0x24D0 + 97)}</span>', s)
        if style == "b":
            out.append(f"<b>{s}</b>")
        elif style == "hl":
            out.append(f'<span class="hl">{s}</span>')
        elif style == "x":
            out.append(f'<span class="x">{s}</span>')
        elif style == "o":
            out.append(f'<span class="ok">{s}</span>')
        elif style == "tag":
            out.append(f'<span class="tag t-{TAG_CLASS.get(s, "m")}">{s}</span>')
        elif style == "blank":
            if MODE["teacher"]:
                out.append(f'<span class="blank fill">{s}</span>')
            else:
                out.append(f'<span class="blank" style="width:{blank_len(s):.1f}em"></span>')
        else:
            out.append(s)
    return "".join(out)


def page(body, part_color="#2B59C3", tint="#EEF3FC", cls=""):
    if MODE["teacher"]:
        cls += " teacher"
    return f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">
<style>{CSS.replace("FONT_DIR", FONT_DIR)}</style></head>
<body class="{cls}" style="--c:{part_color};--tint:{tint}">{body}</body></html>"""


# ---------- 블록 ----------

def r_table(b):
    cols = ""
    if b["widths"]:
        cols = "<colgroup>" + "".join(f'<col style="width:{w}%">' for w in b["widths"]) + "</colgroup>"
    head = "".join(f'<th class="{"ctr" if i in b["center"] else ""}">{inline(h)}</th>' for i, h in enumerate(b["head"]))
    rows = []
    for row in b["rows"]:
        tds = "".join(
            f'<td class="{"ctr" if i in b["center"] else ""}">{inline(c)}</td>' for i, c in enumerate(row))
        rows.append(f"<tr>{tds}</tr>")
    cap = f'<div class="cap">{inline(b["caption"])}</div>' if b["caption"] else ""
    return f'<div class="tbl">{cap}<table>{cols}<thead><tr>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'


def r_ex(b):
    items = "".join(
        f'<li><div class="en">{inline(en)}</div><div class="ko">{inline(ko)}</div></li>' for en, ko in b["items"])
    title = f'<div class="box-title">{escape(b["title"])}</div>' if b["title"] else ""
    return f'<div class="ex">{title}<ol>{items}</ol></div>'


def r_parse(b):
    segs = []
    for text, label in b["segs"]:
        if label:
            segs.append(f'<span class="seg seg-{TAG_CLASS.get(label, "m")}"><span class="w">{escape(text)}</span>'
                        f'<span class="lab">{escape(label)}</span></span>')
        else:
            segs.append(f'<span class="seg seg-none"><span class="w">{escape(text)}</span><span class="lab">&nbsp;</span></span>')
    ko = f'<div class="ko">{inline(b["ko"])}</div>' if b["ko"] else ""
    return f'<div class="parse"><div class="segs">{"".join(segs)}</div>{ko}</div>'


def r_box(kind, label, title, lines):
    lis = "".join(f"<li>{inline(l)}</li>" for l in lines)
    return (f'<div class="box {kind}"><div class="box-head"><span class="badge">{label}</span>'
            f'<span class="box-title">{inline(title)}</span></div><ul>{lis}</ul></div>')


def r_warn(b):
    rows = "".join(
        f'<div class="wrow"><div class="wx"><i>✗</i>{inline(w)}</div><div class="wo"><i>✓</i>{inline(r)}</div>'
        f'<div class="why">{inline(y)}</div></div>' for w, r, y in b["items"])
    return (f'<div class="box warn"><div class="box-head"><span class="badge">주의</span>'
            f'<span class="box-title">{escape(b["title"])}</span></div>{rows}</div>')


def r_q(q, n):
    opts = ""
    if q["options"]:
        opts = '<div class="opts">' + "".join(
            f"<div><span class=\"cn\">{CIRCLED[i]}</span> {inline(o)}</div>" for i, o in enumerate(q["options"])) + "</div>"
    lines = '<div class="wline"></div>' * q["lines"]
    return f'<li class="q"><span class="qn">{n:02d}</span><div class="qb"><div>{inline(q["prompt"])}</div>{opts}{lines}</div></li>'


def r_check(b, unit_no):
    html = [f'<section class="check"><div class="check-head"><span>CHECK-UP</span><em>Unit {unit_no:02d} 확인 문제</em></div>']
    n = 1
    for step, desc, qs in b["steps"]:
        html.append(f'<div class="step"><span class="step-chip">{step}</span><span class="step-desc">{escape(desc)}</span></div><ol class="qs">')
        for q in qs:
            html.append(r_q(q, n))
            n += 1
        html.append("</ol>")
    html.append("</section>")
    return "".join(html)


def r_pilgi(b):
    lis = "".join(f"<li>{inline(l)}</li>" for l in b["lines"])
    return (f'<div class="pilgi"><div class="pilgi-head"><span class="pen">✓</span>{escape(b["title"])}'
            f'<em>수업 필기</em></div><ul>{lis}</ul></div>')


def r_quick(b):
    lis = "".join(f"<li>{inline(l)}</li>" for l in b["lines"])
    return f'<div class="quick"><div class="quick-head">▶ {escape(b["title"])}</div><ul>{lis}</ul></div>'


def r_chain(b):
    rows = []
    for i, (label, sent, note) in enumerate(b["steps"]):
        if i:
            rows.append(f'<div class="ch-arrow"><span>↓</span>{inline(note) if note else ""}</div>')
        rows.append(f'<div class="ch-row"><span class="ch-tag">{inline(label)}</span><span class="ch-s">{inline(sent)}</span></div>')
    return f'<div class="chain"><div class="chain-head">↻ {escape(b["title"])}</div>{"".join(rows)}</div>'


def r_link(b):
    return f'<div class="link"><span class="link-u">Unit {b["unit"]:02d}</span>{inline(b["text"])}</div>'


def render_blocks(blocks, unit_no):
    out = []
    for b in blocks:
        t = b["t"]
        if t == "h":
            out.append(f'<h2>{inline(b["text"])}</h2>')
        elif t == "p":
            out.append(f'<p>{inline(b["text"])}</p>')
        elif t == "formula":
            sub = f'<div class="sub">{inline(b["sub"])}</div>' if b["sub"] else ""
            out.append(f'<div class="formula"><span class="badge">공식</span><div class="f">{inline(b["text"])}</div>{sub}</div>')
        elif t == "table":
            out.append(r_table(b))
        elif t == "ex":
            out.append(r_ex(b))
        elif t == "parse":
            out.append(r_parse(b))
        elif t == "tip":
            out.append(r_box("tip", "TIP", b["title"], b["lines"]))
        elif t == "note":
            out.append(r_box("note", "보충", b["title"], b["lines"]))
        elif t == "list":
            out.append(r_box("note", "정리", b["title"] or "", b["items"]))
        elif t == "warn":
            out.append(r_warn(b))
        elif t == "check":
            out.append(r_check(b, unit_no))
        elif t == "fig":
            cap = f'<figcaption>{inline(b["caption"])}</figcaption>' if b["caption"] else ""
            out.append(f'<figure class="fig">{b["html"]}{cap}</figure>')
        elif t == "tnote":
            if MODE["teacher"]:
                out.append(r_box("note tnote", "교사 메모", b["title"], b["lines"]))
        elif t == "anchor":
            note = f'<div class="an-note">{inline(b["note"])}</div>' if b["note"] else ""
            out.append(f'<div class="anchor"><div class="an-label">이 단원의 기준 문장</div>'
                       f'<div class="an-s">{inline(b["s"])}</div><div class="an-ko">{inline(b["ko"])}</div>{note}</div>')
        elif t == "pilgi":
            out.append(r_pilgi(b))
        elif t == "quick":
            out.append(r_quick(b))
        elif t == "chain":
            out.append(r_chain(b))
        elif t == "link":
            out.append(r_link(b))
        elif t == "stepup":
            out.append(f'<div class="stepup"><span>STEP UP</span><em>심화</em><i>{inline(b["text"])}</i></div>')
        elif t == "pb":
            out.append('<div class="pb"></div>')
    return "\n".join(out)


def stars(level):
    return "★" * level + '<span class="off">' + "★" * (3 - level) + "</span>"


def unit_html(u):
    pno, pname, pen, color, tint = PARTS[u["part"]]
    goals = "".join(f"<li>{inline(g)}</li>" for g in u["goals"])
    opener = f"""
<header class="opener">
  <div class="op-top"><span class="part-chip">{pno} · {pname}</span><span class="level">난이도 {stars(u['level'])}</span></div>
  <div class="op-main"><div class="op-num"><small>UNIT</small>{u['no']:02d}</div>
    <div class="op-title"><h1>{escape(u['title'])}</h1><div class="en">{escape(u['en'])}</div></div></div>
  {f'<p class="intro">{inline(u["intro"])}</p>' if u["intro"] else ""}
  {f'<div class="goals"><div class="goals-title">학습 목표</div><ol>{goals}</ol></div>' if goals else ""}
</header>"""
    test = ""
    if u.get("test"):
        test = ('<div class="pb"></div>' if u["blocks"] else "") + test_html(u["test"], "실전 TEST", f'Unit {u["no"]:02d} {u["title"]}')
    return page(opener + render_blocks(u["blocks"], u["no"]) + test, color, tint, "unit")


def cover_html(units):
    parts = []
    for pid, (pno, pname, pen, color, tint) in PARTS.items():
        names = " · ".join(escape(u["title"]) for u in units if u["part"] == pid)
        parts.append(f'<div class="cv-part" style="--c:{color};--tint:{tint}"><b>{pno}</b><span>{pname}</span><em>{names}</em></div>')
    body = f"""
<div class="cover">
  <div class="cv-series">{BOOK['series']}</div>
  <div class="cv-chips"><span class="tag t-s">S</span><span class="tag t-v">V</span><span class="tag t-o">O</span><span class="tag t-c">C</span><span class="tag t-m">M</span></div>
  <h1 class="cv-title">{BOOK['title']}</h1>
  <div class="cv-en">{BOOK['en']}</div>
  <div class="cv-sub">{BOOK['sub']}</div>
  <div class="cv-ed">{MODE['book'] + ' · ' if MODE['book'] else ''}{'교사용 · 정답 포함' if MODE['teacher'] else '학생용'}</div>
  <div class="cv-parts">{''.join(parts)}</div>
  <div class="cv-foot"><span>개념 정리</span><span>예문 분석</span><span>흔한 실수</span><span>CHECK-UP</span><span>정답·해설</span></div>
</div>"""
    return page(body, cls="cover-page")


GUIDE = {True: "판서 표 → ✓ 필기 포인트 → 도식 → ↻ 한 문장 변형하기 → ▶ 바로 구별하는 법",
         False: "CHECK-UP (기본·어법·바꿔 쓰기) → 실전 TEST → PART 종합 TEST → 실전 모의고사"}


def toc_html(units, pages):
    out = ['<div class="toc"><div class="toc-head"><span>CONTENTS</span><h1>목차</h1></div>']
    for pid, (pno, pname, pen, color, tint) in PARTS.items():
        us = [u for u in units if u["part"] == pid]
        if not us:
            continue
        out.append(f'<div class="toc-part" style="--c:{color};--tint:{tint}"><div class="tp-head"><b>{pno}</b>'
                   f'<span>{pname}</span><em>{pen}</em></div>')
        for u in us:
            pg = pages.get(u["key"], "")
            out.append(f'<div class="tu"><span class="tu-no">{u["no"]:02d}</span><span class="tu-t">{escape(u["title"])}'
                       f'<small>{escape(u["en"])}</small></span><span class="tu-lv">{stars(u["level"])}</span>'
                       f'<span class="dots"></span><span class="tu-pg">{pg}</span></div>')
        if f"part{pid}" in pages:
            out.append(f'<div class="tu tu-test"><span class="tu-no">✓</span><span class="tu-t">{pno} 종합 TEST</span>'
                       f'<span class="tu-lv"></span><span class="dots"></span><span class="tu-pg">{pages[f"part{pid}"]}</span></div>')
        out.append("</div>")
    extras = [(k, t) for k, t in (("mock1", "실전 모의고사 1회"), ("mock2", "실전 모의고사 2회"),
                                  ("appendix", "부록 <small>불규칙 동사표 · 문법 용어 사전</small>"),
                                  ("answers", "정답 및 해설")) if k in pages]
    if extras:
        out.append('<div class="toc-part toc-ans">')
        for k, t in extras:
            out.append(f'<div class="tu"><span class="tu-no">+</span><span class="tu-t">{t}</span>'
                       f'<span class="tu-lv"></span><span class="dots"></span><span class="tu-pg">{pages[k]}</span></div>')
        out.append('</div>')
    out.append('<div class="toc-guide"><b>교재 구성</b><span>' + GUIDE[MODE['book'] == '개념편'] + '</span>'
               '<span>난이도 ★☆☆ 기초 · ★★☆ 핵심 · ★★★ 심화</span></div></div>')
    return page("".join(out), cls="toc-page")


def answers_html(units):
    out = ['<div class="answers"><div class="ans-head"><span>ANSWERS</span><h1>정답 및 해설</h1></div><div class="ans-cols">']
    for u in units:
        color = PARTS[u["part"]][3]
        out.append(f'<div class="ans-unit" style="--c:{color}"><h3>Unit {u["no"]:02d} {escape(u["title"])}</h3>')
        bl = []
        for b in u["blocks"]:
            if b["t"] == "pilgi":
                for l in b["lines"]:
                    bl += blanks(l)
        if bl:
            out.append('<div class="ans-step">필기 포인트 빈칸</div><div class="ans-blanks">'
                       + " · ".join(f"<b>{i}</b> {escape(x)}" for i, x in enumerate(bl, 1)) + "</div>")
        n = 1
        for b in u["blocks"]:
            if b["t"] != "check":
                continue
            for step, desc, qs in b["steps"]:
                out.append(f'<div class="ans-step">{step} {escape(desc)}</div>')
                for q in qs:
                    exp = f'<div class="exp">{inline(q["explain"])}</div>' if q["explain"] else ""
                    out.append(f'<div class="ans"><span class="qn">{n:02d}</span><div><b>{inline(q["answer"])}</b>{exp}</div></div>')
                    n += 1
        out.append("</div>")
    out.append("</div></div>")
    return page("".join(out), cls="ans-page")


def appendix_html(blocks):
    head = '<div class="ans-head"><span>APPENDIX</span><h1>부록</h1></div>'
    return page(head + render_blocks(blocks, 0), "#1E2433", "#F0F2F6", "unit appendix")


# ---------- 실전 TEST ----------

CIRCLED5 = "①②③④⑤"


def test_total(test):
    return sum(it["points"] for it in test["items"])


def r_test_item(it, n):
    tags = f'<span class="lv">{escape(it["level"])}</span>' + ('<span class="hot">고난도</span>' if it["hard"] else "")
    kind = '<span class="wr-tag">서술형</span>' if it["k"] == "wr" else ""
    html = [f'<div class="ti"><div class="ti-q"><span class="ti-n">{n}</span><div>{kind}{inline(it["prompt"])} '
            f'{tags}<span class="pt">({it["points"]}점)</span></div></div>']
    if it["passage"]:
        html.append(f'<div class="ti-passage">{inline(it["passage"])}</div>')
    if it["k"] == "mc":
        row = " row" if max(len(o) for o in it["options"]) <= 8 else ""
        html.append(f'<ol class="ti-opts{row}">' + "".join(
            f'<li><span>{CIRCLED5[i]}</span>{inline(o)}</li>' for i, o in enumerate(it["options"])) + "</ol>")
    else:
        if it["conditions"]:
            html.append('<div class="ti-cond"><b>&lt;조건&gt;</b>' + "".join(
                f"<div>· {inline(c)}</div>" for c in it["conditions"]) + "</div>")
        html.append('<div class="wline"></div>' * it["lines"])
    if MODE["teacher"]:
        ans = CIRCLED5[it["answer"] - 1] if it["k"] == "mc" else inline(it["answer"])
        html.append(f'<div class="t-ans"><b>정답 {ans}</b> {inline(it["explain"])}</div>')
    html.append("</div>")
    return "".join(html)


def test_html(test, label, sub):
    items = test["items"]
    n_mc = sum(1 for it in items if it["k"] == "mc")
    meta = f'{len(items)}문항 · 객관식 {n_mc} · 서술형 {len(items) - n_mc}'
    if test.get("time"):
        meta += f' · 제한시간 {escape(test["time"])}'
    body = "".join(r_test_item(it, i) for i, it in enumerate(items, 1))
    return (f'<section class="test"><div class="test-head"><div><span class="test-label">{escape(label)}</span>'
            f'<h2 class="test-title">{escape(test["title"])}</h2><div class="test-meta">{escape(sub)} · {meta}</div></div>'
            f'<div class="test-score"><div>이름 <i></i></div><div>점수 <i></i> / {test_total(test)}</div></div></div>'
            f'<div class="test-cols">{body}</div></section>')


def test_page_html(test, label, sub, color="#1E2433", tint="#F0F2F6"):
    return page(test_html(test, label, sub), color, tint, "unit test-page")


def test_answers(test, title, color):
    items = test["items"]
    grid = "".join(f'<span><b>{i}</b> {CIRCLED5[it["answer"] - 1] if it["k"] == "mc" else "서술"}</span>'
                   for i, it in enumerate(items, 1))
    exps = "".join(
        f'<div class="ans"><span class="qn">{i:02d}</span><div><b>'
        f'{CIRCLED5[it["answer"] - 1] if it["k"] == "mc" else inline(it["answer"])}</b>'
        f'<div class="exp">{inline(it["explain"])}</div></div></div>' for i, it in enumerate(items, 1))
    return (f'<div class="ans-unit" style="--c:{color}"><h3>{escape(title)}</h3>'
            f'<div class="ans-grid">{grid}</div>{exps}</div>')


def booklet_html(units, part_tests, mocks):
    """정답·해설 별책: CHECK-UP + 필기 빈칸 + 실전 TEST + 파트 종합 + 모의고사"""
    out = ['<div class="answers"><div class="ans-head"><span>ANSWER BOOKLET</span><h1>정답 및 해설</h1></div><div class="ans-cols">']
    base = answers_html(units).split('<div class="ans-cols">', 1)[1].rsplit("</div></div>", 1)[0]
    out.append(base)
    for u in units:
        if u.get("test"):
            out.append(test_answers(u["test"], f'실전 TEST · Unit {u["no"]:02d} {u["title"]}', PARTS[u["part"]][3]))
    for pid, t in part_tests.items():
        out.append(test_answers(t, f'{PARTS[pid][0]} 종합 TEST', PARTS[pid][3]))
    for i, t in enumerate(mocks, 1):
        out.append(test_answers(t, f'실전 모의고사 {i}회', "#1E2433"))
    out.append("</div></div>")
    return page("".join(out), cls="ans-page")
