#!/usr/bin/env python3
import os
import sys
import re

def do_args():
    import argparse
    parser = argparse.ArgumentParser(description='set your MacOS location based on the connected SSID')
    parser.add_argument('-v', '--verbose', help='verbosity',action='store_true')
    args = parser.parse_args()
    return args

def execute(input):
    import subprocess
    import shlex
    r = subprocess.run(shlex.split(input), capture_output=True)
    return(r.stdout)
   
def fetch_ssid():
    l_result = []
    command = '/usr/sbin/ioreg -l' #| grep "IO80211SSID"'
    registry = execute(command)
    registry = registry.decode().split('\n')
    for line in registry:
        if 'IO80211SSID' in line:
            wb = {}
            params = re.search(r'.*\"(?P<ssid>[a-zA-Z0-9\-_]*)\"', line)
            wb = params.groupdict()
            return(wb['ssid'])

def set_location(ssid):
    if ssid in d_prefs['home_networks']:
        location = d_prefs['macos_location']
    else:
        location = 'Automatic'
    command = "/usr/sbin/scselect {}".format(location)
    print(command)
    result = execute("/usr/sbin/scselect {}".format(location))
    print(result.decode)

def main():
    ssid = fetch_ssid()
    set_location(ssid)

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