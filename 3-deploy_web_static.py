#!/usr/bin/python3
""" Creates a tar with the webstatic """
from fabric.api import local, env
from fabric.operations import run, put
import os
import time

env.hosts = ["35.237.94.227", "35.231.144.217"]
env.user = "ubuntu"
env.key_filename = '~/.ssh/key_holberton'


def do_pack():
    """Make a tar.gz archive of da (a directory under ./web_static/)."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    o = local("tar -zvcf ./versions/web_static_%s.tgz ./web_static/"
              % (time.strftime("%Y%m%d%H%M%S", time.gmtime())))
    return o


def do_deploy(archive_path):
    """ Makes the deploy  """
    if not os.path.isfile(archive_path):
        return False
    try:
        filename = archive_path.split("/")[1]
        nefilename = filename.split(".")[0]
        path = "/data/web_static/releases/"+nefilename
        put(archive_path, "/tmp/"+filename)  # send file to servers
        run("mkdir -p /data/web_static/releases/"+nefilename)
        run("tar -xzf /tmp/"+filename+" -C "+path)
        run("rm /tmp/"+filename)  # remove temporal fle
        run("mv "+path+"/web_static/* "+path+"/")
        run("rm -rf "+path+"/web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s "+path+" /data/web_static/current")
        return True
    except Exception:
        return False


def deploy():
    """ Makes the full deployment """
    packed = do_pack()
    if not packed:
        return False
    return do_deploy(packed)
