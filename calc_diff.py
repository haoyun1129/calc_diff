#!/usr/bin/env python3

import fileinput
import sys
import argparse

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more version is required.")

parser = argparse.ArgumentParser()
parser.add_argument('--max', help='threshold of max value, print if out of range', type=float)
parser.add_argument('--min', help='threshold of min value, print if out of range', type=float)
parser.add_argument('--scale', help='multiple by, to adjust the value', type=float)
parser.add_argument('file', metavar='FILE', help='files to read, if empty, stdin is used')
parser.add_argument('--verbose', help='Output verbosely', action='store_true')
args = parser.parse_args()

threshold_max = sys.float_info.min
threshold_min = sys.float_info.max
scale = None
if args.max:
    threshold_max = args.max

if args.min:
    threshold_min = args.min

if args.scale:
    scale = args.scale

prev_value = 0

for line in fileinput.input(args.file):
    line = line.strip()
    value = float(line)
    if scale:
        value *= scale
    if args.verbose:
        print("value:", value)
    diff = value - prev_value
    if diff > threshold_max or diff < threshold_min:
        if not args.verbose:
            print("value:", prev_value)
        print(diff)
        if not args.verbose:
            print("value:", value)

    prev_value = value

