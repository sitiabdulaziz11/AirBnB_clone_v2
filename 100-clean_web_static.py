from fabric import Connection, task
from fabric.api import env, local, put, run, runs_once
import os

# Define your server hosts
env.hosts = ['xx-web-01', 'xx-web-02']  # Replace with your actual server IPs

@task
def do_clean(c, number=0):
    """ Clean up old archives, keeping only the most recent 'number' archives """
    number = int(number)
    
    # Set minimum number of archives to keep to 1
    if number <= 0:
        number = 1
    
    # Local cleanup of old archives
    local_archive_dir = 'versions'
    local_command = "ls -1t {} | tail -n +{}".format(local_archive_dir, number + 1)
    archives_to_delete = c.local(local_command, hide=True).stdout.strip().split('\n')
    
    for archive in archives_to_delete:
        if archive:
            c.local('rm {}'.format(os.path.join(local_archive_dir, archive)))

    # Remote cleanup of old archives on servers
    for host in env.hosts:
        with Connection(host) as conn:
            releases_dir = '/data/web_static/releases'
            remote_command = "ls -1t {} | tail -n +{}".format(releases_dir, number + 1)
            remote_archives_to_delete = conn.run(remote_command, hide=True).stdout.strip().split('\n')
            
            for remote_archive in remote_archives_to_delete:
                if remote_archive:
                    conn.run('rm -rf {}/{}'.format(releases_dir, remote_archive))

    print("Old archives cleaned up successfully!")
