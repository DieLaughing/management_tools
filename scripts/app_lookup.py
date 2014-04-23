#!/usr/bin/env python

import sys

from helpful_tools.app_info import AppInfo

def main (args):
    for item in args[1:]:
        try:
            info = AppInfo(item)
        except ValueError, e:
            info = "Invalid identifier: '" + item + "'"
        print info

if __name__ == "__main__":
    main(sys.argv)
