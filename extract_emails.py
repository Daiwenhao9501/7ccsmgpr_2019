#! /usr/bin/env python3.6

import os, sys

if len(sys.argv) != 2:
    sys.stderr.write("Usage: extract_emails.py <group name>\n")
    sys.exit(1)

with open(os.path.join(sys.argv[1], "members.txt"), "r") as f:
    emails = []
    for l in f:
        l = l.strip()
        if len(l) > 0:
            emails.append(l.split("\t")[2].strip())
    print(", ".join(emails))
