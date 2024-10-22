#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to my web servers, using
the function do_deploy:
"""

import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once

env.hosts = ['54.87.172.4, 100.26.209.47']


def do_pack():
    """
    Make .tgz archive or compressed file on web_static folder.
    """
    if not os.path.exists("versions"):
        local("mkdir versions")
    present_time = datetime.now()
    result = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            present_time.year,
            present_time.month,
            present_time.day,
            present_time.hour,
            present_time.minute,
            present_time.second
            )
    try:
        print("Packing web_static to {}".format(result))
        local("tar -cvzf {} web_static".format(result))
        arch_size = os.stat(result).st_size
        print("web_static packed: {} -> {} Bytes".format(result, arch_size))
    except Exception:
        result = None
    return result


# not work with fabric 3.x

def do_deploy(archive_path):
    """Fabric script that distributes an archive to my
    web servers using the do_deploy function
    """

    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
