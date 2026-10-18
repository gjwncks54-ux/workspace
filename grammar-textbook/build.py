"""교재 빌드: python3 build.py            → 작성된 전체 단원
            python3 build.py 1 2 3      → 지정 단원만
결과: dist/기초영어문법_{개념편,문제편}_{학생용,교사용} .pdf .docx + 기초영어문법_정답해설.pdf (별책)
"""
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from textbook.meta import UNITS  # noqa: E402


def load_units(only=None):
    units = []
    for no, (key, part, title, en, level) in enumerate(UNITS, 1):
        if only and no not in only:
            continue
        try:
            m = importlib.import_module(f"textbook.content.{key}")
        except ModuleNotFoundError:
            continue
        units.append(dict(key=key, no=no, part=part, title=title, en=en, level=level,
                          goals=m.GOALS, intro=m.INTRO, blocks=m.BLOCKS, test=load_test(f"unit_{key}")))
    return units


KEEP_OUT = {"anchor", "link", "tnote", "check"}


def concept_units(units):
    """개념편: STEP UP 전까지의 핵심만 (기준 문장·단원 연결·교사 메모·문제 제외), 학습 목표·도입 설명 제외"""
    out = []
    for u in units:
        core = []
        for b in u["blocks"]:
            if b["t"] == "stepup":
                break
            if b["t"] not in KEEP_OUT:
                core.append(b)
        out.append({**u, "blocks": core, "test": None, "goals": [], "intro": ""})
    return out


def problem_units(units):
    """문제편: 단원별 CHECK-UP + 실전 TEST"""
    return [{**u, "blocks": [b for b in u["blocks"] if b["t"] == "check"], "goals": [], "intro": ""} for u in units]


def load_test(name):
    """textbook/tests/<name>.py 의 TEST (없으면 None)"""
    try:
        return importlib.import_module(f"textbook.tests.{name}").TEST
    except ModuleNotFoundError:
        return None


def main():
    only = {int(a) for a in sys.argv[1:]} or None
    units = load_units(only)
    print("단원:", ", ".join(f'{u["no"]:02d} {u["title"]}' for u in units))
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)

    from textbook import render_docx, render_html
    from textbook.render_pdf import build_booklet, build_pdf
    from textbook.render_docx import build_docx
    from textbook.content.appendix import BLOCKS as appendix
    parts = {p: t for p in range(1, 6) if (t := load_test(f"part_{p}"))}
    mocks = [t for k in (1, 2) if (t := load_test(f"mock_{k}"))]
    if only:
        parts, mocks = {}, []
    from textbook.render_pdf import rasterize_figs
    render_docx.FIG_PATHS.update(rasterize_figs(units, dist / "_figs"))
    books = {
        "개념편": (concept_units(units), appendix, {}, []),
        "문제편": (problem_units(units), None, parts, mocks),
    }
    for book, (us, apx, pt, mk) in books.items():
        for ed, teacher in (("학생용", False), ("교사용", True)):
            render_html.MODE.update(teacher=teacher, book=book)
            render_docx.MODE.update(teacher=teacher, book=book)
            name = f"기초영어문법_{book}_{ed}"
            pages = build_pdf(us, dist / f"{name}.pdf", apx, pt, mk, with_answers=teacher)
            build_docx(us, dist / f"{name}.docx", apx, pt, mk, with_answers=teacher)
            print(name, "완료, 시작 쪽:", pages)
    render_html.MODE["teacher"] = False
    build_booklet(units, parts, mocks, dist / "기초영어문법_정답해설.pdf")
    print("정답 별책 완료")


if __name__ == "__main__":
    main()
