#!/usr/bin/python3
from datetime import datetime
from fabric.api import run, hosts, local, env


@hosts(['142.44.167.237'])
def do_pack():
    """ do_pack - create a compressed tar file """

    env.host_string = '142.44.167.237'
    env.user = "ubuntu"
    env.key_filename = "~/.ssh/holberton_key"

    now = datetime.now().strftime("%Y%m%d%H%M%S")
    fn = "web_static_" + now + ".tgz"

    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(fn))
    if result.failed:
        return None
    else:
        return(fn)
