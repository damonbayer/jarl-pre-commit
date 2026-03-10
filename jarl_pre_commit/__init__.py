import shutil
import subprocess
import sys
from pathlib import Path


def main():
    # Use jarl from PATH if available (e.g., system-installed or user-installed)
    jarl = shutil.which("jarl")

    # Fall back to the binary bundled during hook installation
    if jarl is None:
        pkg_dir = Path(__file__).parent
        binary_name = "jarl.exe" if sys.platform == "win32" else "jarl"
        bundled = pkg_dir / binary_name
        if not bundled.exists():
            print(
                f"jarl binary not found. "
                f"Expected it at {bundled} or on PATH.",
                file=sys.stderr,
            )
            sys.exit(1)
        jarl = str(bundled)

    result = subprocess.run([jarl, "check"] + sys.argv[1:])
    sys.exit(result.returncode)
