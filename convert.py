from pathlib import Path
import pandas as pd

SPREADSHEET = Path("Rocknix_RGARC_RK3566_Yabadabadoo_Saturn_Compatibility.ods")
README = Path("README.md")

START = "<!-- COMPATIBILITY_TABLE_START -->"
END = "<!-- COMPATIBILITY_TABLE_END -->"


def markdown_cell(value):
    """Convert a cell value to safe, readable GitHub Markdown."""
    value = str(value).replace("\r\n", "\n").replace("\r", "\n")
    value = value.replace("\\", "\\\\").replace("|", r"\|")
    value = value.replace("\n", "<br>")
    return value


def main():
    if not SPREADSHEET.exists():
        raise FileNotFoundError(f"Spreadsheet not found: {SPREADSHEET}")

    # First row contains the four column headings.
    df = pd.read_excel(
        SPREADSHEET,
        engine="odf",
        header=0,
        dtype=str,
        keep_default_na=False,
    )

    # Drop fully empty rows, but retain rows with blank notes.
    df = df.loc[
        ~df.apply(lambda row: all(not str(v).strip() for v in row), axis=1)
    ]

    if df.empty or len(df.columns) != 4:
        raise ValueError(
            f"Expected a non-empty table with four columns; found {len(df.columns)}."
        )

    headers = [markdown_cell(column) for column in df.columns]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]

    for _, row in df.iterrows():
        cells = [markdown_cell(value) for value in row]
        lines.append("| " + " | ".join(cells) + " |")

    table = "\n".join(lines)
    readme_text = README.read_text(encoding="utf-8")

    if readme_text.count(START) != 1 or readme_text.count(END) != 1:
        raise ValueError(
            "README.md must contain exactly one COMPATIBILITY_TABLE_START "
            "and one COMPATIBILITY_TABLE_END marker."
        )

    before, rest = readme_text.split(START, 1)
    _, after = rest.split(END, 1)
    updated = before + START + "\n\n" + table + "\n\n" + END + after

    if updated != readme_text:
        README.write_text(updated, encoding="utf-8")
        print(f"Updated README.md with {len(df)} game entries.")
    else:
        print(f"README.md already up to date ({len(df)} game entries).")


if __name__ == "__main__":
    main()
