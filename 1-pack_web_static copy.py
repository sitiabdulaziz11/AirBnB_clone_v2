#!/usr/bin/python3

# not working with fabric 2.x , only for fabric 1.x

"""
A  Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime
import os


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
