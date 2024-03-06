#!/usr/bin/python3
"""
pack web statics
"""
import os
from fabric.api import local, runs_once
from datetime import datetime
env.hosts = ['100.25.3.60', '100.26.157.67']

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


def do_deploy(archive_path):
    """
    deploy static
    """
    if not os.path.exists(archive_path):
        return False
    filee = os.path.basename(archive_path)
    folder = filee.replace(".tgz", "")
    fullPathextr = "/data/web_static/releases/{}/".format(folder)
    try:
        put(archive_path, "/tmp/{}".format(filee))
        run("sudo mkdir -p {}".format(fullPathextr))
        run("sudo tar -xzf /tmp/{} -C {}".format(filee, fullPathextr))
        run("sudo rm -rf /tmp/{}".format(filee))
        run("sudo mv {}web_static/* {}".format(fullPathextr, fullPathextr))
        run("sudo rm -rf {}web_static".format(fullPathextr))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(fullPathextr))
        
        print('New version deployed!')
        return True
    except Exception:
        return False
