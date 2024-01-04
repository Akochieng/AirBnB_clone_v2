#!/usr/bin/python3
'''Uses fabric to compress and archive webstatic contents '''
from fabric import task
from datetime import datetime


def do_pack(c):
    '''a task to compress and archive webstatic files'''
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    c.local("mkdir -p versions")
    result = c.local(f"tar cvzf versions/{timestamp}.tgz /data/web_static")
    if result.failed:
        return None
    return f"versions/{timestamp}.tgz"
