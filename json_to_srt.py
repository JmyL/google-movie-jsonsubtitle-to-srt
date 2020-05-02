#!/usr/bin/python

import sys
import io
from pathlib import Path
import json
from datetime import datetime


def t2s(millisecond):
    return datetime.fromtimestamp(millisecond/1000 + -60*60).strftime('%H:%M:%S,%f')[:-3]


# f.write 'Number of arguments:', len(sys.argv), 'arguments.'
# f.write 'Argument List:', str(sys.argv)
json_filename = '8 해리포터와 죽음의 성물 파트2.json'
if len(sys.argv) > 1:
    json_filename = sys.argv[1]

srt_filename = Path(json_filename).stem + '.srt'

with open(json_filename, 'r') as f:
    subtitles = json.load(f)

with io.open(srt_filename, 'w', newline='\r\n') as f:

    cnt = 0
    for info in subtitles['events']:
        cnt += 1
        f.write(str(cnt) + '\n')
        f.write("{} --> {}\n".format(t2s(info['tStartMs']),
                                     t2s(info['tStartMs'] + info['dDurationMs'])))
        f.write(info['segs'][0]['utf8'] + '\n\n')
        # 00:00:01,120 --> 00:00:05,420
        # f.write(info)

        # "tStartMs": 2931412,
        # "dDurationMs": 2794,
        # "segs": [ {
