#!/usr/bin/python

import sys
import io
from pathlib import Path
import json
import datetime
import pysrt


def t2s(datetime_object):
    return datetime_object.strftime('%H:%M:%S,%f')[:-3]


def s2t(datetime_string):
    return datetime.datetime.strptime(datetime_string, '%H:%M:%S,%f')


# f.write 'Number of arguments:', len(sys.argv), 'arguments.'
# f.write 'Argument List:', str(sys.argv)
ref_file = '8 해리포터와 죽음의 성물 파트2.srt'
trg_file = '8 해리포터와 죽음의 성물 파트2 - Deutsch.srt'
if len(sys.argv) > 2:
    ref_file = sys.argv[1]
    trg_file = sys.argv[2]

# datetime_object = s2t('00:00:28,174')
# print(t2s(datetime_object+datetime.timedelta(milliseconds=1)))
out_file = Path(trg_file).stem + ' - Time Corrected.srt'


def get_start_time(filename):
    with open(filename, 'r') as f:
        f.readline()
        return s2t(f.readline()[:12])


print(t2s(get_start_time(trg_file)))
print(t2s(get_start_time(ref_file)))
time_shift = get_start_time(trg_file) - get_start_time(ref_file)
print(time_shift.total_seconds())

subs = pysrt.open(trg_file, encoding='utf-8-sig')
# Move all subs 2 seconds earlier
subs.shift(seconds=-time_shift.total_seconds())
subs.save(out_file)
