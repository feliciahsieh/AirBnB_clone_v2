#!/usr/bin/python3
from datetime import datetime
from fabric.api import local, run, env


def do_pack():
    """ do_pack - create a compressed tar file """
    """ Ref: https://gist.github.com/elliottb/7744008 """

    # remote ssh credentials
    env.hosts = ['142.44.167.237']
    env.user = 'ubuntu'
    env.key_filename = '~/.ssh/holberton_key'

    # specify path to files being deployed
    env.archive_source = '/data/web_static'

    # archive name, arbitrary, and only for transport
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    env.archive_name = "web_static_" + now + ".tgz"

    result = run("mkdir versions")
    if result.failed:
        return None

    # specify path to deploy root dir - you need to create this
    env.deploy_project_root = '/data/web_static/'

    # specify name of dir that will hold all deployed code
    env.deploy_release_dir = 'versions/'

    # symlink name. Full path to deployed code is env.deploy_project_root + this
    env.deploy_current_dir = 'current'

    result = local("tar -cvzf {} web_static".format(env.archive_name))
    if result.failed:
        return None
    else:
        return(env.archive_name)
