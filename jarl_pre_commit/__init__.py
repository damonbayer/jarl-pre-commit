import subprocess
import sys
from pathlib import Path


def main():
    pkg_dir = Path(__file__).parent
    binary_name = "jarl.exe" if sys.platform == "win32" else "jarl"
    jarl = pkg_dir / binary_name
    if not jarl.exists():
        print(
            f"jarl binary not found at {jarl}.",
            file=sys.stderr,
        )
        sys.exit(1)

    result = subprocess.run([str(jarl), "check"] + sys.argv[1:])
    sys.exit(result.returncode)
