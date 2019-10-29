#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

 # TODO: write your function here
















# DONT MODIFY ANYTHING BELOW THIS COMMENT
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('size', nargs='?', type=int, help='size of the ascii art puzzle')

    args = parser.parse_args()

    if args.size:
        ascii_t(args.size)
    else:
        ascii_t()
