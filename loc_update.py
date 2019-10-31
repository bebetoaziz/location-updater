#!/usr/bin/env python3
import os
import sys

def do_args():
    import argparse
    parser = argparse.ArgumentParser(description='set your MacOS location based on the connected SSID')
    parser.add_argument('-v', '--verbose', help='verbosity',action='store_true')
    args = parser.parse_args()
    return args

def main():
    pass

def set_prefs():
    import json
    pref_file = os.path.abspath(sys.path[0] + '/preferences.json')
    with open(pref_file) as f:
        d_prefs = json.load(f)
    f.close()
    return d_prefs

if __name__ == '__main__':
    args = do_args()
    d_prefs = set_prefs()
    main()