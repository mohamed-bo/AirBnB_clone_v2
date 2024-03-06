#!/usr/bin/python3
"""
pack web statics
"""
import os
from fabric.api import local, runs_once
from datetime import datetime


@runs_once
def do_pack():
    """Archives static"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    nowtime = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        nowtime.year,
        nowtime.month,
        nowtime.day,
        nowtime.hour,
        nowtime.minute,
        nowtime.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        outsize = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, outsize))
    except Exception:
        output = None
    return output
