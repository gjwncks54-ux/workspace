"""신규 단원 검수본: python3 build_review.py → dist/검수/신규단원_검수본.pdf
교재 본편(meta.UNITS)에는 들어가지 않음. 승인 후 meta.UNITS에 등록해 병합."""
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

# (모듈, 파트, 제목, 영문, 난이도, 병합 시 들어갈 위치 메모)
NEW_UNITS = [
    ("u19", 1, "대명사", "Pronouns", 2, "Unit 01 품사 뒤"),
    ("u16", 2, "조동사", "Modal Verbs", 2, "Unit 05 시제 뒤"),
    ("u18", 4, "명사절 / 간접의문문", "Noun Clauses", 3, "Unit 11 관계사 앞"),
    ("u20", 4, "접속사 / 병렬", "Conjunctions & Parallelism", 2, "명사절 뒤"),
    ("u17", 5, "비교", "Comparison", 2, "PART 5 맨 앞"),
]


def main():
    from textbook import render_html
    from textbook.render_pdf import build_pdf
    units = []
    for i, (key, part, title, en, level, where) in enumerate(NEW_UNITS):
        m = importlib.import_module(f"textbook.content.{key}")
        units.append(dict(key=key, no=16 + i, part=part, title=f"{title}", en=f"{en} · 병합 위치: {where}",
                          level=level, goals=m.GOALS, intro=m.INTRO, blocks=m.BLOCKS, test=None))
    out = ROOT / "dist" / "검수"
    out.mkdir(parents=True, exist_ok=True)
    for ed, teacher in (("교사용", True), ("학생용", False)):
        render_html.MODE.update(teacher=teacher, book="신규 단원 검수본")
        build_pdf(units, out / f"신규단원_검수본_{ed}.pdf", None, {}, [], with_answers=teacher, print_files=False)
        print(ed, "완료")


if __name__ == "__main__":
    main()
