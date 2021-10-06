import tkinter as tk
from pathlib import Path
from tkinter import filedialog

CD = Path()


def prompt_for_file(title: str, start_dir: Path = CD) -> Path:  # pragma: no cover
    """Open a Tk file selection dialog to prompt the user to select a single file for processing."""
    root = tk.Tk()
    root.withdraw()

    picked = filedialog.askopenfilename(  # type: ignore[no-untyped-call]  # stubs need mypy bump
        title=title,
        initialdir=start_dir,
        multiple=False,
        filetypes=[
            ("AltiForce Backpack Data", "*.csv"),
            ("All Files", "*.*"),
        ],
    )

    if not picked:
        raise ValueError("No file selected for parsing, aborting.")

    return Path(picked)


def prompt_for_dir(start_dir: Path = CD) -> Path:  # pragma: no cover
    """Open a Tk file selection dialog to prompt the user to select a directory for processing."""
    root = tk.Tk()
    root.withdraw()

    picked = filedialog.askdirectory(  # type: ignore[no-untyped-call]  # stubs need mypy bump
        title="Select directory for batch processing",
        initialdir=start_dir,
    )

    if not picked:
        raise ValueError("No directory selected for parsing, aborting.")

    return Path(picked)
