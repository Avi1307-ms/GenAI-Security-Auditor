import subprocess
import sys


def get_changed_files(base_ref: str) -> list[str]:
    """Return the files changed between origin/<base_ref> and HEAD."""
    result = subprocess.run(
        ["git", "diff", "--name-only", f"origin/{base_ref}...HEAD"],
        capture_output=True,
        text=True,
        check=True,
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def main() -> None:
    base_ref = sys.argv[1] if len(sys.argv) > 1 else "main"
    files = get_changed_files(base_ref)
    print(f"Changed files: {len(files)}")
    for f in files:
        print(f" - {f}")


if __name__ == "__main__":
    main()