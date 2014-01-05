#!/usr/bin/env python

import requests
import sys

print requests.post(sys.argv[1], params={
    'format': 'json',
    'action': 'scribunto-console',
    'title': '-',
    'question': sys.stdin.read(),
}).json()['print']