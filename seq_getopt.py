# seq_getopt.py

from typing import List, Tuple
import getopt
import sys

USAGE = f"Usage: python {sys.argv[0]} [--help] | [-s <sep>] [first [incr]] last"
VERSION = f"{sys.argv[0]} version 1.0.0"

def seq(operands: List[int], sep: str = "\n") -> str:
    first, increment, last = 1, 1, 1
    if len(operands) == 1:
        last = operands[0]
    elif len(operands) == 2:
        first, last = operands
        if first > last:
            increment = -1
    elif len(operands) == 3:
        first, increment, last = operands
    last = last - 1 if first > last else last + 1
    return sep.join(str(i) for i in range(first, last, increment))

def parse(args: List[str]) -> Tuple[str, List[int]]:
    options, arguments = getopt.getopt(
        args,                              # Arguments
        'vhs:',                            # Short option definitions
        ["version", "help", "separator="]) # Long option definitions
    separator = "\n"
    for o, a in options:
        if o in ("-v", "--version"):
            print(VERSION)
            sys.exit()
        if o in ("-h", "--help"):
            print(USAGE)
            sys.exit()
        if o in ("-s", "--separator"):
            separator = a
    if not arguments or len(arguments) > 3:
        raise SystemExit(USAGE)
    try:
        operands = [int(arg) for arg in arguments]
    except:
        raise SystemExit(USAGE)
    return separator, operands

def main() -> None:
    args = sys.argv[1:]
    if not args:
        raise SystemExit(USAGE)
    sep, operands = parse(args)
    print(seq(operands, sep))

if __name__ == "__main__":
    main()