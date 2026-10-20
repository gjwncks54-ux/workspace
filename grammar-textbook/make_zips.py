"""배포용 zip 만들기 (한글 파일명 UTF-8 표시 → 윈도우·카톡에서 안 깨짐)
python3 grammar-textbook/make_zips.py  → workspace/제본용.zip, workspace/grammar-textbook-src.zip
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent


def pack(dst, files, base):
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:  # 비ASCII 이름은 zipfile이 UTF-8 플래그를 자동으로 켬
        for f in sorted(files):
            z.write(f, f.relative_to(base).as_posix())


bind = ROOT / "dist" / "제본용"
pack(OUT / "제본용.zip", [f for f in bind.iterdir() if f.is_file()], bind)  # 폴더 없이 파일만
pack(OUT / "grammar-textbook-src.zip",
     [f for f in ROOT.rglob("*") if f.is_file() and "__pycache__" not in f.parts and "_figs" not in f.parts], ROOT.parent)
print("완료")
