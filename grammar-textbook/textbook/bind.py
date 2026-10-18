"""제본용 파일: dist/제본용/
책마다 ① 본문 PDF (중철이면 4의 배수로 맞춤) ② 펼침 표지 PDF (뒤표지 | 책등 | 앞표지, 도련 3mm) + 제본_사양서.txt
"""
import base64
import io
import math
import shutil
from pathlib import Path

from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4

from textbook import render_html as R
from textbook.meta import BIND, BOOK, PARTS
from textbook.render_pdf import CHROMIUM, ROOT

W, H = 210, 297


def spine_mm(pages, saddle):
    if saddle:
        return 0
    return math.ceil((pages / 2 * BIND["leaf_mm"] + BIND["cover_mm"]) * 2) / 2  # 0.5mm 단위 올림


def back_html(units, book):
    logo = base64.b64encode((ROOT / "assets" / "del-logo.png").read_bytes()).decode()
    parts = "".join(
        f'<div class="bk-part" style="--c:{c}"><b>{pno}</b><span>{pname}</span>'
        f'<em>{" · ".join(u["title"] for u in units if u["part"] == pid)}</em></div>'
        for pid, (pno, pname, _, c, _) in PARTS.items())
    return f"""
<div class="bk-in">
  <div class="cv-series">{BOOK['series']}</div>
  <h2 class="bk-title">외워서 바로 푼다.</h2>
  <p class="bk-lead">복잡한 설명은 빼고, 문제를 푸는 데 필요한 <b>공식</b>만 남겼습니다.<br>
  수업 판서 그대로의 표 · 한 문장 변형 · 판별 공식으로 중·고등 문법을 정리합니다.</p>
  <div class="bk-parts">{parts}</div>
  <div class="bk-books"><span>개념편</span><span>문제편</span><span>정답 및 해설</span></div>
  <div class="bk-foot"><img src="data:image/png;base64,{logo}"><span>{book}</span></div>
</div>"""


SPREAD_CSS = """
@page {{ size: {w}mm {h}mm; margin: 0; }}
html, body {{ margin: 0; }}
.spread {{ display: flex; width: {w}mm; height: {h}mm; }}
.panel {{ width: {pw}mm; height: {h}mm; overflow: hidden; position: relative; }}
.panel.front .cover {{ width: {pw}mm; height: {h}mm; box-sizing: border-box; padding: 29mm 25mm 23mm 22mm; }}
.panel.back {{ background: #1E2433; color: #fff; }}
.bk-in {{ box-sizing: border-box; height: 100%; padding: 29mm 22mm 23mm 25mm; display: flex; flex-direction: column; }}
.bk-in .cv-series {{ color: #8FB0FF; }}
.bk-title {{ font-size: 26pt; font-weight: 800; margin: 26mm 0 6mm; letter-spacing: -1px; }}
.bk-lead {{ font-size: 10.5pt; line-height: 1.8; color: #C9D1E3; margin: 0; }}
.bk-lead b {{ color: #fff; }}
.bk-parts {{ margin-top: 16mm; display: flex; flex-direction: column; gap: 3mm; }}
.bk-part {{ display: grid; grid-template-columns: 18mm 26mm 1fr; align-items: baseline; border-left: 3px solid var(--c); padding-left: 4mm; }}
.bk-part b {{ font-size: 8pt; color: #8A93A6; letter-spacing: .08em; }}
.bk-part span {{ font-weight: 800; font-size: 10pt; }}
.bk-part em {{ font-style: normal; font-size: 8pt; color: #C9D1E3; }}
.bk-books {{ margin-top: auto; display: flex; gap: 6px; }}
.bk-books span {{ font-size: 8pt; font-weight: 700; border: 1px solid #4A5470; border-radius: 12px; padding: 2px 10px; color: #C9D1E3; }}
.bk-foot {{ margin-top: 8mm; display: flex; align-items: center; justify-content: space-between; }}
.bk-foot img {{ width: 52mm; filter: brightness(0) invert(1); opacity: .85; }}
.bk-foot span {{ font-size: 9pt; font-weight: 700; color: #8A93A6; }}
.spine {{ width: {sw}mm; height: {h}mm; background: #2B59C3; color: #fff; display: flex; align-items: center;
          justify-content: space-between; writing-mode: vertical-rl; padding: 28mm 0; box-sizing: border-box; overflow: hidden;
          font-size: {sf}pt; font-weight: 800; white-space: nowrap; }}
.spine small {{ font-size: {sf2}pt; font-weight: 600; opacity: .85; }}
"""


def cover_spread(pg, units, book, label, sw, out):
    b = BIND["bleed_mm"]
    pw = W + b
    w, h = pw * 2 + sw, H + 2 * b
    front = R.cover_html(units, label).split("<body", 1)[1].split(">", 1)[1].rsplit("</body>", 1)[0]
    spine = ""
    if sw:
        text = f'<span>{BOOK["title"]}  <small>{label}</small></span><small>{BOOK["series"]}</small>' if sw >= 5 else ""
        spine = f'<div class="spine">{text}</div>'
    css = SPREAD_CSS.format(w=w, h=h, pw=pw, sw=sw, sf=min(sw * 2.2, 14), sf2=min(sw * 1.4, 9))
    html = R.page(f'<div class="spread"><div class="panel back">{back_html(units, label)}</div>{spine}'
                  f'<div class="panel front">{front}</div></div>', cls="cover-page")
    pg.set_content(html.replace("</style>", css + "</style>"), wait_until="load")
    pg.evaluate("document.fonts.ready")
    out.write_bytes(pg.pdf(width=f"{w}mm", height=f"{h}mm", print_background=True,
                           margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}))
    return w, h


def build_binding(units, dist: Path, file_stem: str):
    out = dist / "제본용"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir()
    jobs = [  # (번호, 책 이름, 표지 라벨, 본문 원본)
        ("1", "개념편_학생용", "개념편 · 학생용", dist / "인쇄용" / f"{file_stem}_개념편_학생용_본문.pdf"),
        ("2", "문제편_학생용", "문제편 · 학생용", dist / "인쇄용" / f"{file_stem}_문제편_학생용_본문.pdf"),
        ("3", "정답해설", "정답 및 해설 (별책)", dist / f"{file_stem}_정답해설.pdf"),
        ("4", "개념편_교사용", "개념편 · 교사용 · 정답 포함", dist / "인쇄용" / f"{file_stem}_개념편_교사용_본문.pdf"),
        ("5", "문제편_교사용", "문제편 · 교사용 · 정답 포함", dist / "인쇄용" / f"{file_stem}_문제편_교사용_본문.pdf"),
    ]
    lines = [f"{BOOK['title']} ({BOOK['series']}) — 제본 사양서", "=" * 44, "",
             "공통", "- 판형: A4 (210 × 297mm), 본문 컬러 인쇄",
             f"- 표지: 펼침 1장 (뒤표지 | 책등 | 앞표지), 사방 도련 {BIND['bleed_mm']}mm 포함",
             "- 본문: 도련 없음 (모든 요소가 여백 안쪽), 글꼴 전부 임베드",
             f"- 책등 두께 계산: 쪽수 ÷ 2 × {BIND['leaf_mm']}mm + {BIND['cover_mm']}mm (모조 80g 가정)",
             "  → 인쇄소에서 종이별 실제 책등 두께를 받으면 meta.py BIND 값을 고쳐 다시 만들 것", ""]
    with sync_playwright() as pw:
        br = pw.chromium.launch(executable_path=CHROMIUM)
        pg = br.new_page()
        for no, name, label, src in jobs:
            r = PdfReader(src)
            body = PdfWriter()
            for p in r.pages:
                body.add_page(p)
            saddle = len(body.pages) <= BIND["saddle_max"]
            mult = 4 if saddle else 2
            while len(body.pages) % mult:
                body.add_blank_page(*A4)
            n = len(body.pages)
            buf = io.BytesIO()
            body.write(buf)
            (out / f"{no}_{file_stem}_{name}_본문.pdf").write_bytes(buf.getvalue())
            sw = spine_mm(n, saddle)
            w, h = cover_spread(pg, units, name, label, sw, out / f"{no}_{file_stem}_{name}_표지.pdf")
            lines += [f"[{no}] {name.replace('_', ' ')}",
                      f"- 본문 {n}쪽" + (f" (빈 면 {n - len(r.pages)}쪽 추가)" if n > len(r.pages) else ""),
                      f"- 제본: {'중철 (스테이플)' if saddle else '무선 (본드)'}",
                      f"- 책등: {sw}mm" if sw else "- 책등: 없음 (중철)",
                      f"- 표지 펼침 크기: {w:g} × {h:g}mm (재단 후 {w - 2 * BIND['bleed_mm']:g} × {H}mm)", ""]
        br.close()
    (out / "제본_사양서.txt").write_text("\n".join(lines), encoding="utf-8")
    return out
