import argparse
import sys
from pathlib import Path

import nbformat


def normalize_notebook(path, check=False):
    notebook = nbformat.read(path, as_version=4)
    changed = False

    for cell in notebook.cells:
        if cell.cell_type == "code":
            if cell.outputs or cell.execution_count is not None:
                changed = True
            cell.outputs = []
            cell.execution_count = None

    nbformat.validate(notebook)
    if check and changed:
        print(f"Notebook has outputs or execution counts: {path}", file=sys.stderr)
        return 1
    if not check:
        nbformat.write(notebook, path)
        print(f"Notebook validated and normalized: {path}")
    else:
        print(f"Notebook is clean and valid: {path}")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("notebook", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    raise SystemExit(normalize_notebook(args.notebook, args.check))


if __name__ == "__main__":
    main()
