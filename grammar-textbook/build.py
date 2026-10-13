"""교재 빌드: python3 build.py            → 작성된 전체 단원
            python3 build.py 1 2 3      → 지정 단원만
결과: dist/기초영어문법_학생용/교사용 .pdf .docx
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
                          goals=m.GOALS, intro=m.INTRO, blocks=m.BLOCKS))
    return units


def main():
    only = {int(a) for a in sys.argv[1:]} or None
    units = load_units(only)
    print("단원:", ", ".join(f'{u["no"]:02d} {u["title"]}' for u in units))
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)

    from textbook import render_docx, render_html
    from textbook.render_pdf import build_pdf
    from textbook.render_docx import build_docx
    from textbook.content.appendix import BLOCKS as appendix
    for ed, teacher in (("학생용", False), ("교사용", True)):
        render_html.MODE["teacher"] = render_docx.MODE["teacher"] = teacher
        pages = build_pdf(units, dist / f"기초영어문법_{ed}.pdf", appendix)
        build_docx(units, dist / f"기초영어문법_{ed}.docx", appendix)
        print(ed, "완료, 시작 쪽:", pages)


if __name__ == "__main__":
    main()
