#!/usr/bin/env python3.6

import argparse

#build the parser
parser = argparse.ArgumentParser(description="Read a file in reverse")
parser.add_argument("filename", help ="the file to read")
parser.add_argument("--limit","-l", type=int, help = "the number of lines to read")
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()


#parse the arguments
with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()

    if args.limit:
        lines = lines[:args.limit]

    for line in lines:
        print(line.strip()[::-1])
