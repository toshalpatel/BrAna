#!/usr/bin/env python
import json

with open('test_run.txt') as f:
    with open('desTestRun.txt','w') as f1:
        for line in f:
            resp_dict = json.loads(line)
            d = resp_dict['text']
            f1.write(d)

f1.close()
f.close()
