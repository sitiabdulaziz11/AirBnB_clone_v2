# from pack_web_static import do_pack

#!/usr/bin/python3
"""
A Fabric script that generates a.tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric import task, Connection
from datetime import datetime
import os
import subprocess


@task
def do_pack(c):
    """
    Make.tgz archive or compressed file from the web_static folder.
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
        subprocess.check_call(["tar", "-cvzf", archive_name, "web_static"])
        archive_size = os.stat(archive_name).st_size
        print("web_static packed: {} -> {} Bytes".format(archive_name, archive_size))
        return archive_name
    except Exception as e:
        print(f"Error: {e}")
        return None



# Define the remote hosts (web servers)
env_hosts = ['<IP web-01>', '<IP web-02>']   # must be replaced

@task
def do_deploy(c, archive_path):
    """
    Distributes an archive to web servers
    Args:
        c: Connection object (auto-passed by Fabric 3)
        archive_path (str): The path to the archive file
    Returns:
        bool: True if all operations are successful, False otherwise
    """
    # Check if the file exists
    if not os.path.exists(archive_path):
        print("Archive path does not exist")
        return False

    try:
        # Extract archive filename and folder name (without extension)
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = archive_filename.split(".")[0]
        remote_tmp_path = f"/tmp/{archive_filename}"

        # Upload the archive to the /tmp/ directory on the web server
        print(f"Uploading {archive_filename} to /tmp/ on the server")
        c.put(archive_path, remote_tmp_path)

        # Create the target release folder
        remote_release_path = f"/data/web_static/releases/{archive_no_ext}/"
        print(f"Creating release folder {remote_release_path}")
        c.run(f"mkdir -p {remote_release_path}")

        # Uncompress the archive to the folder
        print(f"Uncompressing {archive_filename} into {remote_release_path}")
        c.run(f"tar -xzf {remote_tmp_path} -C {remote_release_path}")

        # Remove the archive from the server
        print(f"Removing the archive from {remote_tmp_path}")
        c.run(f"rm {remote_tmp_path}")

        # Move the contents of the web_static folder to the release folder
        print("Moving files to the release folder")
        c.run(f"mv {remote_release_path}web_static/* {remote_release_path}")
        c.run(f"rm -rf {remote_release_path}web_static")

        # Delete the old symbolic link
        print("Deleting old symbolic link /data/web_static/current")
        c.run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        print(f"Creating new symbolic link /data/web_static/current to {remote_release_path}")
        c.run(f"ln -s {remote_release_path} /data/web_static/current")

        print("New version deployed successfully!")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False
