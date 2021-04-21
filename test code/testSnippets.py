from pathlib import Path

for fname in Path('./txt').iterdir():
    if fname.stem.endswith("-sc"):
        print(fname, "has the keyword")


