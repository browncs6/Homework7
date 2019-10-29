#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

# TODO: create a ascii_hline function

# TODO: create a ascii_vline function

# TODO: copy over your ascii_t function and remove the default parameter

# TODO: create a ascii_selector function

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('size', nargs='?', type=int, default=1, help='size of the ascii art puzzle')
    parser.add_argument('puzzle', nargs='?', type=str, default='t', help='puzzle choices; includes: hline, vline, or t')

    args = parser.parse_args()

    # TODO: create ascii_functions list 
    # TODO: call ascii_selector function 
