#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using
the function do_deploy:
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.87.172.4, 100.26.209.47']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False

    try:
        file = archive_path.split("/")[-1]
        num_exe = file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, num_exe))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, num_exe))
        run('rm /tmp/{}'.format(file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, num_exe))
        run('rm -rf {}{}/web_static'.format(path, num_exe))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, num_ext))
        return True
    except Exception:
        return False
