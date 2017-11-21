#!/usr/bin/python3
import os, errno
from datetime import datetime
from fabric.api import local, run, env, hosts, local

@hosts(['142.44.167.237'])
def do_pack():
    """ do_pack - create a compressed tar file """

    env.host_string = '142.44.167.237'
    env.user = "ubuntu"
    env.key_filename = "~/.ssh/holberton_key"

    now = datetime.now().strftime("%Y%m%d%H%M%S")
    fn = "web_static_" + now + ".tgz"
    print(fn)

    local("tar -cvzf {} web_static".format(fn))

    result = run("mkdir versions")
    if result.failed:
        return None
    else:
        return(fn)
