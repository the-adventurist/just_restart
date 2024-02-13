# sha1sum_val.py

from typing import List
import hashlib
import pathlib
import sys

def process_file(filename: str) -> bytes:
    return pathlib.Path(filename).read_bytes()

def process_stdin() -> bytes:
    return bytes("".join(sys.stdin), "utf-8")

def sha1sum(data: bytes) -> str:
    m = hashlib.sha1()
    m.update(data)
    return m.hexdigest()

def output_sha1sum(data: bytes, filename: str = "-") -> None:
    print(f"{sha1sum(data)}  {filename}")

def main(args: List[str]) -> None:
    if not args:
        output_sha1sum(process_stdin())
    for arg in args:
        if arg == "-":
            output_sha1sum(process_stdin(), "-")
            continue
        try:
            output_sha1sum(process_file(arg), arg)
        except (FileNotFoundError, IsADirectoryError) as err:
            print(f"{sys.argv[0]}: {arg}: {err.strerror}", file=sys.stderr)

if __name__ == "__main__":
    main(sys.argv[1:])