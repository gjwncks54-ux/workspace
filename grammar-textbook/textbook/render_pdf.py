"""HTML → PDF (Chromium) + 병합 + 쪽번호"""
import io
from pathlib import Path

from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from textbook import render_html as R
from textbook.meta import BOOK, PARTS, WATERMARK

CHROMIUM = "/opt/pw-browsers/chromium"
MARGIN = {"top": "19mm", "bottom": "17mm", "left": "17mm", "right": "17mm"}


def header(left, right, color):
    return (f'<div style="width:100%;font-family:Pretendard,sans-serif;font-size:7.5px;padding:0 17mm;'
            f'display:flex;justify-content:space-between;color:#8A93A6;-webkit-print-color-adjust:exact">'
            f'<span style="letter-spacing:.06em">{left}</span>'
            f'<span style="color:{color};font-weight:700">{right}</span></div>')


def _pdf(pg, html, head=None, margin=MARGIN):
    pg.set_content(html, wait_until="load")
    pg.evaluate("document.fonts.ready")
    kw = dict(format="A4", print_background=True, margin=margin, prefer_css_page_size=False)
    if head:
        kw.update(display_header_footer=True, header_template=head, footer_template="<div></div>")
    return pg.pdf(**kw)


ROOT = Path(__file__).resolve().parent.parent


def watermark_page():
    """WATERMARK 사양대로 로고 한 장짜리 PDF 페이지 생성 (투명 배경 유지, 알파에 불투명도 곱함)"""
    if not WATERMARK.get("enabled"):
        return None
    from PIL import Image
    from reportlab.lib.utils import ImageReader
    im = Image.open(ROOT / WATERMARK["image"]).convert("RGBA")
    alpha = im.getchannel("A").point(lambda a: round(a * WATERMARK["opacity"]))
    im.putalpha(alpha)
    w, h = A4
    iw = WATERMARK["width_pt"]
    ih = iw * im.height / im.width
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    c.drawImage(ImageReader(im), (w - iw) / 2, (h - ih) / 2, iw, ih, mask="auto")
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]


def number_pages(reader, start_index, first_no):
    """start_index 페이지부터 쪽번호(바깥쪽 아래) 찍기"""
    w, h = A4
    writer = PdfWriter()
    wm = watermark_page()
    for i, p in enumerate(reader.pages):
        if wm is not None:
            p.merge_page(wm)
        if i >= start_index:
            no = first_no + i - start_index
            buf = io.BytesIO()
            c = canvas.Canvas(buf, pagesize=A4)
            c.setFillColorRGB(0.54, 0.58, 0.65)
            c.setFont("Helvetica", 6.5)
            label = BOOK["series"]
            if no % 2:  # 홀수쪽 오른쪽
                c.setFont("Helvetica-Bold", 9)
                c.setFillColorRGB(0.12, 0.14, 0.2)
                c.drawRightString(w - 17 * 2.835, 9 * 2.835, str(no))
                c.setFont("Helvetica", 6.5)
                c.setFillColorRGB(0.54, 0.58, 0.65)
                c.drawRightString(w - 17 * 2.835 - 16, 9 * 2.835 + 1, label)
            else:
                c.setFont("Helvetica-Bold", 9)
                c.setFillColorRGB(0.12, 0.14, 0.2)
                c.drawString(17 * 2.835, 9 * 2.835, str(no))
                c.setFont("Helvetica", 6.5)
                c.setFillColorRGB(0.54, 0.58, 0.65)
                c.drawString(17 * 2.835 + 16, 9 * 2.835 + 1, label)
            c.save()
            buf.seek(0)
            p.merge_page(PdfReader(buf).pages[0])
        writer.add_page(p)
    return writer


def build_pdf(units, out_path: Path, appendix=None, part_tests=None, mocks=None, with_answers=True):
    part_tests, mocks = part_tests or {}, mocks or []
    with sync_playwright() as pw:
        br = pw.chromium.launch(executable_path=CHROMIUM)
        pg = br.new_page()

        sections = []  # (key, pdf bytes)
        for i, u in enumerate(units):
            pno, pname, _, color, tint = PARTS[u["part"]]
            head = header(f'{BOOK["series"]} · {pno} {pname}', f'Unit {u["no"]:02d}  {u["title"]}', color)
            sections.append((u["key"], _pdf(pg, R.unit_html(u), head)))
            last_of_part = i == len(units) - 1 or units[i + 1]["part"] != u["part"]
            if last_of_part and u["part"] in part_tests:
                sections.append((f'part{u["part"]}', _pdf(pg, R.test_page_html(
                    part_tests[u["part"]], f"{pno} 종합 TEST", pname, color, tint),
                    header(f'{BOOK["series"]} · {pno} {pname}', f"{pno} 종합 TEST", color))))
        for k, t in enumerate(mocks, 1):
            sections.append((f"mock{k}", _pdf(pg, R.test_page_html(t, f"실전 모의고사 {k}회", "전 범위"),
                                              header(BOOK["series"], f"실전 모의고사 {k}회", "#1E2433"))))
        if appendix:
            sections.append(("appendix", _pdf(pg, R.appendix_html(appendix), header(BOOK["series"], "부록", "#1E2433"))))
        if with_answers:
            ans_head = header(BOOK["series"], "정답 및 해설", "#1E2433")
            sections.append(("answers", _pdf(pg, R.answers_html(units), ans_head)))

        # 쪽번호 계산 (본문 첫 쪽 = 1)
        pages, cur = {}, 1
        for key, data in sections:
            pages[key] = cur
            cur += len(PdfReader(io.BytesIO(data)).pages)

        cover = _pdf(pg, R.cover_html(units), margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        toc = _pdf(pg, R.toc_html(units, pages), margin={"top": "22mm", "bottom": "18mm", "left": "20mm", "right": "20mm"})
        br.close()

    merged = PdfWriter()
    front = 0
    for data in [cover, toc] + [d for _, d in sections]:
        r = PdfReader(io.BytesIO(data))
        for p in r.pages:
            merged.add_page(p)
    front = len(PdfReader(io.BytesIO(cover)).pages) + len(PdfReader(io.BytesIO(toc)).pages)

    buf = io.BytesIO()
    merged.write(buf)
    buf.seek(0)
    final = number_pages(PdfReader(buf), front, 1)
    final.compress_identical_objects(remove_identicals=True, remove_orphans=True)
    final.add_metadata({"/Title": f'{BOOK["title"]} - {BOOK["en"]}', "/Author": BOOK["series"]})
    with open(out_path, "wb") as f:
        final.write(f)
    return pages


def build_booklet(units, part_tests, mocks, out_path: Path):
    """정답·해설 별책"""
    with sync_playwright() as pw:
        br = pw.chromium.launch(executable_path=CHROMIUM)
        pg = br.new_page()
        data = _pdf(pg, R.booklet_html(units, part_tests, mocks), header(BOOK["series"], "정답 및 해설 (별책)", "#1E2433"))
        br.close()
    final = number_pages(PdfReader(io.BytesIO(data)), 0, 1)
    final.add_metadata({"/Title": f'{BOOK["title"]} - 정답 및 해설', "/Author": BOOK["series"]})
    with open(out_path, "wb") as f:
        final.write(f)
