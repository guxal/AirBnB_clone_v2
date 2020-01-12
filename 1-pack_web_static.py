#!/usr/bin/python3
""" Creates a tar with the webstatic """
from fabric.api import local
import os
import time


def do_pack():
    """Make a tar.gz archive of da (a directory under ./web_static/)."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    o = local("tar -zvcf ./versions/web_static_%s.tgz ./web_static/"
              % (time.strftime("%Y%m%d%H%M%S", time.gmtime())))
    return o
