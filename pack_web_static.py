#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric import task
from datetime import datetime
import os

@task(name='do_pack')
def do_pack(c):
    """
    Make .tgz archive or compressed file from the web_static folder.
    """
    if not os.path.exists("versions"):
        os.makedirs("versions")  # Create the directory locally

    present_time = datetime.now()
    archive_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        present_time.year,
        present_time.month,
        present_time.day,
        present_time.hour,
        present_time.minute,
        present_time.second
    )

    try:
        print("Packing web_static to {}".format(archive_name))
        c.local("tar -cvzf {} web_static".format(archive_name))  # Use local shell command
        archive_size = os.stat(archive_name).st_size
        print("web_static packed: {} -> {} Bytes".format(archive_name, archive_size))
        return archive_name
    except Exception as e:
        print(f"Error: {e}")
        return None
